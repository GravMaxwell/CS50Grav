# test_project.py
import pytest
from unittest.mock import patch
from project import get_user_input, adjust_lie, adjust_swing, select_club

def test_adjust_lie():
    assert adjust_lie(100, "Sand") == 95
    assert adjust_lie(100, "Rough") == 90
    assert adjust_lie(100, "Fairway") == 100
    assert adjust_lie(100, "Tee") == 105
    assert adjust_lie(100, "Unknown") == 100

def test_adjust_swing():
    assert adjust_swing(100, "Full") == 100
    assert adjust_swing(100, "3/4") == 75
    assert adjust_swing(100, "Half") == 50
    assert adjust_swing(100, "Quarter") == 25
    assert adjust_swing(100, "Unknown") == 100

def test_select_club():
    club, adjusted_yardage, average_yardage, adjusted_clubs = select_club(150, "Fairway", "Full")
    assert club == "Pitching Wedge"
    assert adjusted_yardage == 135.0
    assert average_yardage == 135.0

    club, adjusted_yardage, average_yardage, adjusted_clubs = select_club(90, "Sand", "Half")
    assert club == "7-Iron"
    assert adjusted_yardage == 85.0
    assert average_yardage == 175.0

@patch('builtins.input', side_effect=["150.5", "Fairway", "Full"])
def test_get_user_input(mock_input):
    yardage, surface, swing = get_user_input()
    assert yardage == 151
    assert surface == "Fairway"
    assert swing == "Full"

