from numb3rs import validate


def test_valid():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True
    assert validate("1.2.3.4") is True


def test_invalid_numbers():
    assert validate("256.0.0.1") is False
    assert validate("1.256.3.4") is False
    assert validate("1.2.256.4") is False
    assert validate("1.2.3.256") is False
    assert validate("-1.2.3.4") is False


def test_invalid_format():
    assert validate("1.2.3") is False
    assert validate("1.2.3.4.5") is False
    assert validate("cat") is False
    assert validate("hello.world") is False
    assert validate("...") is False


def test_edge_cases():
    assert validate("01.02.03.04") is False
    assert validate("255.0.255.0") is True
