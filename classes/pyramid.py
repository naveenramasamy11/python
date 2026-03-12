#!/usr/bin/env python3
"""Pyramid pattern using a class."""


class Pyramid:
    def __init__(self, range_n: int, pattern: str, spaces: str) -> None:
        self.range_n = range_n
        self.pattern = pattern
        self.spaces = spaces

    def convert(self) -> None:
        n = self.range_n
        for i in range(n):
            print((n - i) * self.spaces, end="")
            print(i * self.pattern)
        for i in range(n, -1, -1):
            print((n - i) * self.spaces, end="")
            print(i * self.pattern)


obj = Pyramid(10, " *", " ")
obj.convert()
