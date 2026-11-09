import contextlib
import io
import sys

from countdown import DEFAULT_SECONDS, format_remaining, parse_args

def test_format():
    assert format_remaining(3661) == "01:01:01"
    assert format_remaining(0) == "00:00:00"


def test_seconds_defaults_to_60():
    assert parse_args([]).seconds == DEFAULT_SECONDS == 60


def test_seconds_flag():
    assert parse_args(["--seconds", "10"]).seconds == 10
    assert parse_args(["--seconds", "0"]).seconds == 0


def test_seconds_rejects_bad_values():
    for bad in ("abc", "-5"):
        try:
            with contextlib.redirect_stderr(io.StringIO()):
                parse_args(["--seconds", bad])
        except SystemExit as exc:
            assert exc.code == 2
        else:
            raise AssertionError(f"--seconds {bad} 应当报错退出")


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for test in tests:
        test()
        print(f"ok  {test.__name__}")
    print(f"\n{len(tests)} passed")
    sys.exit(0)
