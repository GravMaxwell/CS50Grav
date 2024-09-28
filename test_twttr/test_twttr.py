import twttr
import pytest
# wrote this at work again hehe PLZ DONT TELL THE BOSSMAN ;)
def test_shorten_lowercase():
    assert twttr.shorten("hello") == "hll"
    assert twttr.shorten("WORLD") == "WRLD"

def test_shorten_mixed_case():
    assert twttr.shorten("HeLLo WoRLd") == "HLL WRLd"

def test_shorten_no_vowels():
    assert twttr.shorten("bcdfg") == "bcdfg"

def test_shorten_only_vowels():
    assert twttr.shorten("aeiouAEIOU") == ""

def test_shorten_empty_string():
    assert twttr.shorten("") == ""

# add a test case to check for numbers (check50 error)
def test_shorten_numbers():
    assert twttr.shorten("1234") == "1234"

# add a test case to check for punctuation (check50 error)
def test_shorten_punctuation():
    assert twttr.shorten(".,!@?") == ".,!@?"

