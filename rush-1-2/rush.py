import sys


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if y == 1:
        print("*" * x)
        return

    if x == 1:
        for _ in range(y):
            print("*")
        return

    print("/" + "*" * (x - 2) + "\\")
    for _ in range(y - 2):
        print("*" + " " * (x - 2) + "*")
    print("\\" + "*" * (x - 2) + "/")
