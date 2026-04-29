"""
Testy pro modul calculator.functions.

Obsahuje unit testy pro všechny matematické funkce.
Spuštění: python -m pytest
"""

import pytest
from maingame.playerLogic import (
    Player, sonar
)


# =============================================================================
# Testy sonar funkce
# =============================================================================

class TestSonar:
    """Testy funkcí pro sonar"""

    def CreateEmptyTestBoard():
        return [['~' for _ in range(8)] for _ in range(8)]

    def test_sonar_pozice_0_0(self):
        emptyTestBoard = self.CreateEmptyTestBoard()

        """Testuje, zda je pozice (0, 0) loďe Destroyer/Submarine  True."""
        assert sonar(emptyTestBoard, 0,0, 3) == True
    
