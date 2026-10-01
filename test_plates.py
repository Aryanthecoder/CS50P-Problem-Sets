from plates import is_valid


def test_length():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("ABCDEFG") == False


def test_start_with_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("5ABC") == False
    assert is_valid("1A") == False
    assert is_valid("50") == False


def test_numbers_at_end():
    assert is_valid("CS50") == True
    assert is_valid("CS5A") == False
    assert is_valid("CS50A") == False


def test_first_number_not_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS01") == False


def test_alphanumeric_only():
    assert is_valid("CS-50") == False
    assert is_valid("HELLO!") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False



