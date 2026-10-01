import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/5") == 0
    assert convert("5/5") == 100


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
