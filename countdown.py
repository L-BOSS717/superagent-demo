"""下班倒计时：给定秒数，打印还剩多久。"""

import argparse

DEFAULT_SECONDS = 60


def format_remaining(seconds: int) -> str:
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def countdown(seconds: int):
    while seconds > 0:
        print(format_remaining(seconds))
        seconds -= 1
    print("下班！")


def _non_negative_int(value: str) -> int:
    try:
        seconds = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"需要一个整数，收到 {value!r}")
    if seconds < 0:
        raise argparse.ArgumentTypeError(f"秒数不能为负数，收到 {seconds}")
    return seconds


def parse_args(argv=None) -> argparse.Namespace:
    """解析命令行参数：--seconds 指定倒计时总秒数，默认 60。"""
    parser = argparse.ArgumentParser(description="下班倒计时")
    parser.add_argument(
        "--seconds",
        type=_non_negative_int,
        default=DEFAULT_SECONDS,
        metavar="N",
        help=f"倒计时总秒数（默认 {DEFAULT_SECONDS}）",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    countdown(parse_args().seconds)
