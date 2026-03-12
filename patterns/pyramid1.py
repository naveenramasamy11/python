#!/usr/bin/env python3
"""Simple pyramid with user-defined range."""


def pyramid(n: int) -> None:
    for i in range(n):
        print(" " * (n - i) + "* " * i)
    for i in range(n, -1, -1):
        print(" " * (n - i) + "* " * i)


pyramid(int(input("Enter the range: ")))
