from seasons import minutes_to_words


def test_zero():
    assert minutes_to_words(0) == "Zero minutes"


def test_thousands():
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"


def test_millions():
    assert minutes_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"


def test_multi_million():
    assert minutes_to_words(2629440) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
