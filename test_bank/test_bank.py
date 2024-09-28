import bank
import pytest

def test_value_hello():
    assert bank.value("hello") == 0
    assert bank.value("Hello") == 0
    assert bank.value("HELLO") == 0

def test_value_h():
    assert bank.value("hi") == 20
    assert bank.value("Hi") == 20
    assert bank.value("HEY") == 20

def test_value_other():
    assert bank.value("what's up") == 100
    assert bank.value("Greetings") == 100
    assert bank.value("Good morning") == 100

def test_value_edge_cases():
    assert bank.value("hello there") == 0
    assert bank.value("hi there") == 20
    assert bank.value("H") == 20
    assert bank.value("H!") == 20

if __name__ == "__main__":
    pytest.main()
