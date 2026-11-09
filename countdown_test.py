from countdown import DEFAULT_SECONDS, format_remaining, parse_args

def test_format():
    assert format_remaining(3661) == "01:01:01"
    assert format_remaining(0) == "00:00:00"

def test_seconds_defaults_to_60():
    assert parse_args([]).seconds == DEFAULT_SECONDS == 60

def test_seconds_flag_overrides():
    assert parse_args(["--seconds", "10"]).seconds == 10
