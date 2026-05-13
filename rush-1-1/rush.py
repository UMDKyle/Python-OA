import sys


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if y == 1:
        if x == 1:
            print("o")
        else:
            print("o" + "-" * (x - 2) + "o")
        return

    top_bot = "o" if x == 1 else "o" + "-" * (x - 2) + "o"
    mid = "|" if x == 1 else "|" + " " * (x - 2) + "|"

    print(top_bot)
    for _ in range(y - 2):
        print(mid)
    print(top_bot)
