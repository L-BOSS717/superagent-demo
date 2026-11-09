from countdown import format_remaining

def test_format():
    assert format_remaining(3661) == "01:01:01"
    assert format_remaining(0) == "00:00:00"
