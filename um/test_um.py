import pytest
from um import  count

def test_single_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_multiple_ums():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3

def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("hello, world") == 0
