"""
Testy pro modul maingame.playerLogic.

Obsahuje unit testy pro ověření funkčnosti třídy Player a funkce sonar.
Spuštění: python -m pytest
"""

import pytest
from maingame.playerLogic import Player, sonar


class TestSonar:
    """Testy pro ověření logiky funkce sonar (validace umístění lodě)."""

    def create_empty_board(self):
        """Pomocná metoda pro vytvoření prázdného pole 8x8."""
        return [['~' for _ in range(8)] for _ in range(8)]

    def test_placement_success_horizontal(self):
        """Test horizontálního umístění (orientation=False) na volné místo."""
        board = self.create_empty_board()
        assert sonar(board, 0, 0, 3, orientation=False) is True

    def test_placement_success_vertical(self):
        """Test vertikálního umístění (orientation=True) na volné místo."""
        board = self.create_empty_board()
        assert sonar(board, 0, 0, 3, orientation=True) is True

    def test_collision_with_other_ship(self):
        """Test, zda funkce detekuje kolizi s existující lodí ('■')."""
        board = self.create_empty_board()
        board[2][0] = '■'
        assert sonar(board, 0, 0, 3, orientation=False) is False

    def test_out_of_bounds_start_coordinates(self):
        """Test souřadnic mimo pole (záporné nebo příliš velké)."""
        board = self.create_empty_board()
        assert sonar(board, -1, 0, 2) is False
        assert sonar(board, 8, 8, 2) is False

    def test_ship_overflow_horizontal(self):
        """Test, kdy loď 'vyčuhuje' z pole doprava."""
        board = self.create_empty_board()
        assert sonar(board, 6, 0, 3, orientation=False) is False

    def test_ship_overflow_vertical(self):
        """Test, kdy loď 'vyčuhuje' z pole dolů."""
        board = self.create_empty_board()
        assert sonar(board, 0, 6, 3, orientation=True) is False

    def test_placement_at_the_very_edge(self):
        """Test umístění těsně k okraji (poslední možná pozice)."""
        board = self.create_empty_board()
        assert sonar(board, 5, 0, 3, orientation=False) is True
        assert sonar(board, 0, 5, 3, orientation=True) is True


class TestPlayerShips:
    """Testy pro ověření umisťování lodí třídou Player."""

    @pytest.mark.parametrize("method_name, ship_index, length", [
        ("place_battleship", 0, 5),
        ("place_cruiser", 1, 4),
        ("place_submarine", 2, 3),
        ("place_destroyer", 3, 3),
    ])
    def test_ship_placement_horizontal(self, method_name, ship_index, length):
        """Testuje horizontální položení pro všechny typy lodí."""
        p = Player("Tester")
        placement_method = getattr(p, method_name)
        placement_method(0, 0, orientation=False)
        for i in range(length):
            assert p.board[i][0] == '■'
        assert p.placed[ship_index] is True

    @pytest.mark.parametrize("method_name, ship_index, length", [
        ("place_battleship", 0, 5),
        ("place_cruiser", 1, 4),
        ("place_submarine", 2, 3),
        ("place_destroyer", 3, 3),
    ])
    def test_ship_placement_vertical(self, method_name, ship_index, length):
        """Testuje vertikální položení pro všechny typy lodí."""
        p = Player("Tester")
        placement_method = getattr(p, method_name)
        placement_method(0, 0, orientation=True)
        for i in range(length):
            assert p.board[0][i] == '■'
        assert p.placed[ship_index] is True

    def test_placement_collision_all_ships(self):
        """Testuje položení lodě tam, kde už nějaká loď je."""
        p = Player("Tester")
        p.board[0][0] = '■'
        p.place_cruiser(0, 0, orientation=False)
        assert p.placed[1] is False


class TestPlayerShoot:
    """Testy pro ověření mechaniky střelby."""

    @pytest.fixture
    def player(self):
        """Vytvoří instanci hráče pro každý test."""
        return Player("Tester")

    @pytest.fixture
    def enemy_board(self):
        """Vytvoří testovací pole nepřítele (8x8)."""
        board = [['~' for _ in range(8)] for _ in range(8)]
        board[3][3] = '■'
        return board

    def test_shoot_hit(self, player, enemy_board):
        """Test úspěšného zásahu lodi."""
        result = player.shoot(enemy_board, 3, 3)
        assert result is True
        assert player.shoot_board[3][3] == 'X'

    def test_shoot_miss(self, player, enemy_board):
        """Test minutí lodi (střela do vody)."""
        result = player.shoot(enemy_board, 0, 0)
        assert result is False
        assert player.shoot_board[0][0] == 'O'

    def test_shoot_repeat_hit(self, player, enemy_board):
        """Test opakované střely na místo, kde už byl zásah (X)."""
        player.shoot(enemy_board, 3, 3)
        result = player.shoot(enemy_board, 3, 3)
        assert result == "Repeat"
        assert player.shoot_board[3][3] == 'X'

    def test_shoot_repeat_miss(self, player, enemy_board):
        """Test opakované střely na místo, kde už bylo minutí (O)."""
        player.shoot(enemy_board, 1, 1)
        result = player.shoot(enemy_board, 1, 1)
        assert result == "Repeat"
        assert player.shoot_board[1][1] == 'O'

    def test_shoot_board_not_leaking(self, player, enemy_board):
        """Ověří, že střela na (0,0) neovlivní okolní pole."""
        player.shoot(enemy_board, 0, 0)
        assert player.shoot_board[0][0] == 'O'
        assert player.shoot_board[0][1] == '~'
        assert player.shoot_board[1][0] == '~'
