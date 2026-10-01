from response import validate


def test_valid():
    assert validate("malan@harvard.edu") == "Valid"
    assert validate("sysadmins@cs50.harvard.edu") == "Valid"
    assert validate("first.last@example.com") == "Valid"


def test_invalid():
    assert validate("malan at harvard dot edu") == "Invalid"
    assert validate("malan@@@harvard.edu") == "Invalid"
    assert validate("malan@harvard") == "Invalid"
    assert validate("") == "Invalid"
