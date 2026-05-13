import sys


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if y == 1 or x == 1:
        for _ in range(y):
            print("B" * x)
        return

    top_bot = "A" + "B" * (x - 2) + "C"
    mid = "B" + " " * (x - 2) + "B"

    print(top_bot)
    for _ in range(y - 2):
        print(mid)
    print(top_bot)
