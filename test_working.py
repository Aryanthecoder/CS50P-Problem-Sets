from working import convert
import pytest

def test_valid_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("1 PM to 1 AM") == "13:00 to 01:00"

def test_valid_minutes():
    assert convert("1:30 PM to 2:45 PM") == "13:30 to 14:45"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("09:00 AM - 05:00 PM")
    with pytest.raises(ValueError):
        convert("5 PM 9 AM")

def test_invalid_numbers():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")       
