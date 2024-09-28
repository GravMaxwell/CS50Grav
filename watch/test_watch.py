import pytest
from watch import parse

def test_valid_youtube_urls():
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"

def test_invalid_youtube_urls():
    assert parse('<iframe src="https://cs50.harvard.edu/python"></iframe>') == None
    assert parse('<iframe src="https://www.example.com/embed/xvFZjo5PgG0"></iframe>') == None
    assert parse('<iframe src="http://youtube.com/embed/"></iframe>') == None
