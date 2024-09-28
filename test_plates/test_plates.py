# once again found myself doing cs50 problems at work again.... performance improvement plan incoming?
import pytest
from plates import is_valid

def test_valid_plate():
    assert is_valid("AB1234") == True
    assert is_valid("XY9876") == True
    assert is_valid("XY") == True
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False
    assert is_valid(" 2") == False


def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_invalid_start():
    assert is_valid("1ABC") == False
    assert is_valid("A1BC") == False

def test_invalid_characters():
    assert is_valid("AB@123") == False
    assert is_valid("AB 123") == False

def test_numbers_at_end():
    assert is_valid("AB123C") == False
    assert is_valid("AB0123") == False


# (check50 error) adding a test case to check for plates that do not start with letters
def test_starts_with_two_letters():
    assert is_valid("123ABC") == False
    assert is_valid("012ABC") == False
    assert is_valid("A1BCDE") == False
    assert is_valid("1ABCDE") == False
    assert is_valid(" ABCDE") == False
