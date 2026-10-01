from watch import parse

def test_valid_embed():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/abc123XYZ"></iframe>') == "https://youtu.be/abc123XYZ"

def test_invalid_embed():

    assert parse('<iframe src="https://www.youtube.com/watch?v=xvFZjo5PgG0"></iframe>') is None

    assert parse('<iframe src="https://vimeo.com/12345"></iframe>') is None

    assert parse('<iframe></iframe>') is None

    assert parse("hello world") is None

def test_edge_cases():

    assert parse('<iframe allowfullscreen src="https://www.youtube.com/embed/ZZZ_123-xyz"></iframe>') == "https://youtu.be/ZZZ_123-xyz"
    
    assert parse('<iframe src="https://youtube.com/embed/qwerty123"></iframe>') == "https://youtu.be/qwerty123"
