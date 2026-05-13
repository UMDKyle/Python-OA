import sys


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if y == 1 or x == 1:
        for _ in range(y):
            print("B" * x)
        return

    print("A" + "B" * (x - 2) + "C")
    for _ in range(y - 2):
        print("B" + " " * (x - 2) + "B")
    print("C" + "B" * (x - 2) + "A")
