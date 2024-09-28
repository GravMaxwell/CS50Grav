import pytest
from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True

def test_invalid_addresses():
    assert validate("275.0.0.1") == False
    assert validate("255.255.255.256") == False
    assert validate("192.168.1.1000") == False
    assert validate("cat") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
