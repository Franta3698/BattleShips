"""
Testy pro modul calculator.functions.

Obsahuje unit testy pro všechny matematické funkce.
Spuštění: python -m pytest
"""

import pytest
from maingame.playerLogic import Player, sonar

import pytest


# =============================================================================
# Testy sonaru
# =============================================================================


class TestSonar:
    """Testy pro ověření logiky funkce sonar (validace umístění lodě)"""

    def create_empty_board(self):
        """Pomocná metoda pro vytvoření prázdného pole 8x8"""
        return [['~' for _ in range(8)] for _ in range(8)]

    # --- ÚSPĚŠNÉ UMÍSTĚNÍ ---

    def test_placement_success_horizontal(self):
        """Test horizontálního umístění (orientation=False) na volné místo"""
        board = self.create_empty_board()
        # Loď délky 3 na (0,0) by měla zabrat (0,0), (1,0), (2,0)
        assert sonar(board, 0, 0, 3, orientation=False) is True

    def test_placement_success_vertical(self):
        """Test vertikálního umístění (orientation=True) na volné místo"""
        board = self.create_empty_board()
        # Loď délky 3 na (0,0) by měla zabrat (0,0), (0,1), (0,2)
        assert sonar(board, 0, 0, 3, orientation=True) is True

    # --- KOLIZE S JINOU LODÍ ---

    def test_collision_with_other_ship(self):
        """Test, zda funkce detekuje kolizi s existující lodí ('■')"""
        board = self.create_empty_board()
        board[2][0] = '■'  # Překážka na cestě
        # Pokus o horizontální umístění přes překážku
        assert sonar(board, 0, 0, 3, orientation=False) is False

    # --- HRANICE POLE (OUT OF BOUNDS) ---

    def test_out_of_bounds_start_coordinates(self):
        """Test souřadnic mimo pole (záporné nebo příliš velké)"""
        board = self.create_empty_board()
        assert sonar(board, -1, 0, 2) is False
        assert sonar(board, 8, 8, 2) is False

    def test_ship_overflow_horizontal(self):
        """Test, kdy loď 'vyčuhuje' z pole doprava"""
        board = self.create_empty_board()
        # Start na x=6, délka 3 -> potřebuje x 6, 7, 8 (8 je mimo)
        assert sonar(board, 6, 0, 3, orientation=False) is False # Pozor: tvůj kód vrací None v tomto případě!

    def test_ship_overflow_vertical(self):
        """Test, kdy loď 'vyčuhuje' z pole dolů"""
        board = self.create_empty_board()
        # Start na y=6, délka 3 -> potřebuje y 6, 7, 8 (8 je mimo)
        assert sonar(board, 0, 6, 3, orientation=True) is False

    # --- OKRAJOVÉ PŘÍPADY ---

    def test_placement_at_the_very_edge(self):
        """Test umístění těsně k okraji (poslední možná pozice)"""
        board = self.create_empty_board()
        # Horizontálně: start 5, délka 3 -> 5, 6, 7 (OK)
        assert sonar(board, 5, 0, 3, orientation=False) is True
        # Vertikálně: start 5, délka 3 -> 5, 6, 7 (OK)
        assert sonar(board, 0, 5, 3, orientation=True) is True

# =============================================================================
# Testy hráče
# =============================================================================


class TestPlayerShips:

    @pytest.mark.parametrize("method_name, ship_index, length", [
        ("placeBattleship", 0, 5),
        ("placeCruiser", 1, 4),
        ("placeSubmarine", 2, 3),
        ("placeDestroyer", 3, 3),
    ])
    def test_ship_placement_horizontal(self, method_name, ship_index, length):
        """Testuje horizontální položení pro všechny typy lodí"""
        p = Player("Tester")
        
        # Dynamicky získáme metodu ze třídy Player podle jejího názvu
        placement_method = getattr(p, method_name)
        
        # Zavoláme metodu
        placement_method(0, 0, orientation=False)
        
        # Ověříme, že je loď na desce
        for i in range(length):
            assert p.Board[i][0] == '■'
            
        # Ověříme, že se správně nastavil příznak v poli Placed
        assert p.Placed[ship_index] is True

    @pytest.mark.parametrize("method_name, ship_index, length", [
        ("placeBattleship", 0, 5),
        ("placeCruiser", 1, 4),
        ("placeSubmarine", 2, 3),
        ("placeDestroyer", 3, 3),
    ])
    def test_ship_placement_vertical(self, method_name, ship_index, length):
        """Testuje vertikální položení pro všechny typy lodí"""
        p = Player("Tester")
        
        placement_method = getattr(p, method_name)
        placement_method(0, 0, orientation=True)
        
        # Ověříme svislou linii
        for i in range(length):
            assert p.Board[0][i] == '■'
            
        assert p.Placed[ship_index] is True

    def test_placement_collision_all_ships(self):
        """
        Testuje položení lodě tam kde už nějaká loď je
        """
        p = Player("Tester")
        p.Board[0][0] = '■' # Preemptivní blokáda
        
        # Zkusíme položit křižník (index 1) na zablokované místo
        p.placeCruiser(0, 0, orientation=False)
        
        assert p.Placed[1] is False

import pytest

class TestPlayerShoot:

    @pytest.fixture
    def player(self):
        """Vytvoří instanci hráče pro každý test"""
        return Player("Tester")

    @pytest.fixture
    def enemy_board(self):
        """Vytvoří testovací pole nepřítele (8x8)"""
        board = [['~' for _ in range(8)] for _ in range(8)]
        board[3][3] = '■'  # Umístíme loď na 3,3
        return board

    def test_shoot_hit(self, player, enemy_board):
        """Test úspěšného zásahu lodi"""
        result = player.shoot(enemy_board, 3, 3)
        
        assert result is True
        assert player.ShootBoard[3][3] == 'X'

    def test_shoot_miss(self, player, enemy_board):
        """Test minutí lodi (střela do vody)"""
        result = player.shoot(enemy_board, 0, 0)
        
        assert result is False
        assert player.ShootBoard[0][0] == 'O'

    def test_shoot_repeat_hit(self, player, enemy_board):
        """Test opakované střely na místo, kde už byl zásah (X)"""
        # První střela - zásah
        player.shoot(enemy_board, 3, 3)
        
        # Druhá střela na stejné místo
        result = player.shoot(enemy_board, 3, 3)
        
        assert result == "Repeat"
        # Ujistíme se, že tam pořád zůstalo 'X'
        assert player.ShootBoard[3][3] == 'X'

    def test_shoot_repeat_miss(self, player, enemy_board):
        """Test opakované střely na místo, kde už bylo minutí (O)"""
        # První střela - voda
        player.shoot(enemy_board, 1, 1)
        
        # Druhá střela na stejné místo
        result = player.shoot(enemy_board, 1, 1)
        
        assert result == "Repeat"
        # Ujistíme se, že tam pořád zůstalo 'O'
        assert player.ShootBoard[1][1] == 'O'

    def test_shoot_board_not_leaking(self, player, enemy_board):
        """Ověří, že střela na (0,0) neovlivní okolní pole"""
        player.shoot(enemy_board, 0, 0)
        
        assert player.ShootBoard[0][0] == 'O'
        assert player.ShootBoard[0][1] == '~'
        assert player.ShootBoard[1][0] == '~'