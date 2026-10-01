from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("hello!") == "hll!"

def test_empty():
    assert shorten("") == ""
