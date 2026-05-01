

"""
Modul pro logiku hry Námořní bitva.

Tento modul definuje třídu Player pro správu herního stavu jednotlivých 
hráčů a pomocnou funkci sonar pro validaci umisťování lodí.

Třídy
-----
Player
    Reprezentace hráče, jeho polí a akcí (střelba, pokládání lodí).

Funkce
------
sonar
    Ověření, zda lze loď na dané souřadnice umístit.
"""





class Player:
    """
    Reprezentuje hráče a jeho herní stav.

    Attributes
    ----------
    Name : str
        Jméno hráče.
    Hp : int
        Počet zbývajících životů (celkový počet polí lodí).
    Board : list
        Dvojrozměrné pole s vlastními loděmi.
    ShootBoard : list
        Dvojrozměrné pole se záznamem střelby na nepřítele.
    Placed : list
        Informace o tom, které lodě již byly umístěny.
    """
    def __init__(self, Name):
        """
        Inicializuje nového hráče.

        Parameters
        ----------
        name : str
            Jméno hráče.
        """
        self.Name = Name
        self.Hp = 15
        self.Board = [['~' for _ in range(8)] for _ in range(8)]
        self.ShootBoard = [['~' for _ in range(8)] for _ in range(8)]
        self.Placed = [False for _ in range(4)]

    def placeBattleship(self, cordX, cordY, orientation = False): #4
        """
        Umístí bitevní loď (velikost 5) na herní pole.

        Parameters
        ----------
        cord_x : int
            Počáteční řádek.
        cord_y : int
            Počáteční sloupec.
        orientation : bool, optional
            Orientace lodi. Výchozí je False.
        """
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
        """
        Umístí bitevní loď (velikost 4) na herní pole.

        Parameters
        ----------
        cord_x : int
            Počáteční řádek.
        cord_y : int
            Počáteční sloupec.
        orientation : bool, optional
            Orientace lodi. Výchozí je False.
        """
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
        """
        Umístí bitevní loď (velikost 3) na herní pole.

        Parameters
        ----------
        cord_x : int
            Počáteční řádek.
        cord_y : int
            Počáteční sloupec.
        orientation : bool, optional
            Orientace lodi. Výchozí je False.
        """
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
    def placeDestroyer(self, cordX, cordY, orientation = False): #3
        """
        Umístí bitevní loď (velikost 3) na herní pole.

        Parameters
        ----------
        cord_x : int
            Počáteční řádek.
        cord_y : int
            Počáteční sloupec.
        orientation : bool, optional
            Orientace lodi. Výchozí je False.
        """
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
        """
        Provede výstřel na zadané pole soupeře.

        Parameters
        ----------
        enemy_board : list
            Herní pole soupeře, na které se střílí.
        cord_x : int
            Cílový řádek.
        cord_y : int
            Cílový sloupec.

        Returns
        -------
        bool or str
            True při zásahu, False při minutí, "Repeat" při opakované střele.

        Examples
        --------
        >>> player.shoot(enemy_board, 0, 0)
        True
        >>> player.shoot(enemy_board, 0, 0)
        'Repeat'
        """
        if self.ShootBoard[cordX][cordY] == 'X' or self.ShootBoard[cordX][cordY] == 'O':
            print("Zadejte pole na které jste ještě nestřílel")
            return "Repeat"
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
        """Vypíše herní pole s vlastními loděmi do konzole."""
        print("TABULKA VAŠICH LODÍ")
        print("  0 1 2 3 4 5 6 7")
        i = 0
        for row in self.Board:
            print(str(i) + " " + str(' '.join(row)))
            i += 1

    def printShootBoard(self):
        """Vypíše pole se zásahy a minutími do konzole."""
        print("TABULKA ZÁSAHŮ LODÍ")
        print("  0 1 2 3 4 5 6 7")
        i = 0
        for row in self.ShootBoard:
            print(str(i) + " " + str(' '.join(row)))
            i += 1
        
        


def sonar(board, cordX, cordY, shipLenght, orientation = False):
    """
    Ověří, zda je možné umístit loď na dané souřadnice.

    Kontroluje, zda loď nepřetéká z herního pole a zda nekoliduje
    s již umístěnými loděmi.

    Parameters
    ----------
    board : list
        Dvojrozměrné pole reprezentující herní desku.
    cord_x : int
        Počáteční řádek (0-7).
    cord_y : int
        Počáteční sloupec (0-7).
    ship_length : int
        Délka umisťované lodi v počtu polí.
    orientation : bool, optional
        Orientace lodi. False pro vodorovnou (šířka), 
        True pro svislou (výška). Výchozí je False.

    Returns
    -------
    bool
        True, pokud je pozice validní, jinak False.
    """
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
                return False
        for i in range(shipLenght):
                if board[cordX + i][cordY] == '■':
                    return False
    return True



if __name__ == "__main__":
    pass