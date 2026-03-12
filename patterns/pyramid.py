#!/usr/bin/env python3
"""Full diamond pyramid using a function."""


def pyramid(x: int) -> None:
    for i in range(x):
        print(" " * (x - i) + "* " * i)
    for i in range(x, -1, -1):
        print(" " * (x - i) + "* " * i)


pyramid(10)
