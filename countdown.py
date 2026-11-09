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


def parse_args(argv=None):
    """解析命令行参数；未指定 --seconds 时从 60 秒开始倒计时。"""
    parser = argparse.ArgumentParser(description="下班倒计时：打印还剩多久")
    parser.add_argument(
        "--seconds",
        type=int,
        default=DEFAULT_SECONDS,
        metavar="N",
        help=f"倒计时的总秒数（默认 {DEFAULT_SECONDS}）",
    )
    args = parser.parse_args(argv)
    if args.seconds < 0:
        parser.error("--seconds 不能为负数")
    return args


if __name__ == "__main__":
    countdown(parse_args().seconds)
