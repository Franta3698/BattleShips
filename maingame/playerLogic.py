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
    name : str
        Jméno hráče.
    hp : int
        Počet zbývajících životů (celkový počet polí lodí).
    board : list
        Dvojrozměrné pole s vlastními loděmi.
    shoot_board : list
        Dvojrozměrné pole se záznamem střelby na nepřítele.
    placed : list
        Informace o tom, které lodě již byly umístěny.
    """

    def __init__(self, name):
        """
        Inicializuje nového hráče.

        Parameters
        ----------
        name : str
            Jméno hráče.
        """
        self.name = name
        self.hp = 15
        self.board = [['~' for _ in range(8)] for _ in range(8)]
        self.shoot_board = [['~' for _ in range(8)] for _ in range(8)]
        self.placed = [False for _ in range(4)]

    def place_battleship(self, cord_x, cord_y, orientation=False):
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
        ship_length = 5
        if sonar(self.board, cord_x, cord_y, ship_length, orientation):
            for i in range(ship_length):
                if orientation:
                    self.board[cord_x][cord_y + i] = '■'
                else:
                    self.board[cord_x + i][cord_y] = '■'
            self.placed[0] = True
        else:
            print("Lodička se nepoložila :(")

    def place_cruiser(self, cord_x, cord_y, orientation=False):
        """
        Umístí křižník (velikost 4) na herní pole.

        Parameters
        ----------
        cord_x : int
            Počáteční řádek.
        cord_y : int
            Počáteční sloupec.
        orientation : bool, optional
            Orientace lodi. Výchozí je False.
        """
        ship_length = 4
        if sonar(self.board, cord_x, cord_y, ship_length, orientation):
            for i in range(ship_length):
                if orientation:
                    self.board[cord_x][cord_y + i] = '■'
                else:
                    self.board[cord_x + i][cord_y] = '■'
            self.placed[1] = True
        else:
            print("Lodička se nepoložila :(")

    def place_submarine(self, cord_x, cord_y, orientation=False):
        """
        Umístí ponorku (velikost 3) na herní pole.

        Parameters
        ----------
        cord_x : int
            Počáteční řádek.
        cord_y : int
            Počáteční sloupec.
        orientation : bool, optional
            Orientace lodi. Výchozí je False.
        """
        ship_length = 3
        if sonar(self.board, cord_x, cord_y, ship_length, orientation):
            for i in range(ship_length):
                if orientation:
                    self.board[cord_x][cord_y + i] = '■'
                else:
                    self.board[cord_x + i][cord_y] = '■'
            self.placed[2] = True
        else:
            print("Lodička se nepoložila :(")

    def place_destroyer(self, cord_x, cord_y, orientation=False):
        """
        Umístí torpédoborec (velikost 3) na herní pole.

        Parameters
        ----------
        cord_x : int
            Počáteční řádek.
        cord_y : int
            Počáteční sloupec.
        orientation : bool, optional
            Orientace lodi. Výchozí je False.
        """
        ship_length = 3
        if sonar(self.board, cord_x, cord_y, ship_length, orientation):
            for i in range(ship_length):
                if orientation:
                    self.board[cord_x][cord_y + i] = '■'
                else:
                    self.board[cord_x + i][cord_y] = '■'
            self.placed[3] = True
        else:
            print("Lodička se nepoložila :(")

    def shoot(self, enemy_board, cord_x, cord_y):
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
        """
        if self.shoot_board[cord_x][cord_y] in ('X', 'O'):
            print("Zadejte pole na které jste ještě nestřílel")
            return "Repeat"

        if enemy_board[cord_x][cord_y] == '■':
            self.shoot_board[cord_x][cord_y] = 'X'
            return True
        else:
            self.shoot_board[cord_x][cord_y] = 'O'
            return False

    def print_board(self):
        """Vypíše herní pole s vlastními loděmi do konzole."""
        print("TABULKA VAŠICH LODÍ")
        print("  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.board):
            print(f"{i} {' '.join(row)}")

    def print_shoot_board(self):
        """Vypíše pole se zásahy a minutími do konzole."""
        print("TABULKA ZÁSAHŮ LODÍ")
        print("  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.shoot_board):
            print(f"{i} {' '.join(row)}")


def sonar(board, cord_x, cord_y, ship_length, orientation=False):
    """
    Ověří, zda je možné umístit loď na dané souřadnice.

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
        False pro vodorovnou (šířka), True pro svislou (výška).

    Returns
    -------
    bool
        True, pokud je pozice validní, jinak False.
    """
    if not (0 <= cord_x <= 7 and 0 <= cord_y <= 7):
        return False

    if orientation:
        if cord_y + ship_length - 1 > 7:
            return False
        for i in range(ship_length):
            if board[cord_x][cord_y + i] == '■':
                return False
    else:
        if cord_x + ship_length - 1 > 7:
            return False
        for i in range(ship_length):
            if board[cord_x + i][cord_y] == '■':
                return False
    return True


if __name__ == "__main__":
    pass
