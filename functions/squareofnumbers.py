#!/usr/bin/env python3
"""Generate a list of squares for numbers 1 through n."""


def squares(n: int) -> list:
    return [i * i for i in range(1, n + 1)]


print(squares(10))
