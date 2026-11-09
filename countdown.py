"""下班倒计时：给定秒数，打印还剩多久。"""

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

if __name__ == "__main__":
    countdown(60)
