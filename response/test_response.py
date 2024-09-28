import pytest
from response import validate_email

def test_valid_emails():
    assert validate_email("malan@harvard.edu") == True
    assert validate_email("user@example.com") == True

def test_invalid_emails():
    assert validate_email("malan@@@harvard.edu") == False
    assert validate_email("user@.com") == False
    assert validate_email("user@com") == False
    assert validate_email("user@domain..com") == False
