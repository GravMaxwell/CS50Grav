import pytest
from datetime import date
from seasons import calculate_minutes, convert_to_words

def test_calculate_minutes():
    assert calculate_minutes(date.today()) == 0
    assert calculate_minutes(date(2022, 1, 1)) == (date.today() - date(2022, 1, 1)).days * 24 * 60

def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert convert_to_words(527040) == "Five hundred twenty-seven thousand forty"


