#!/usr/bin/env python3
"""Filter and return only even numbers from a list."""


def get_only_even(numbers: list) -> list:
    return [n for n in numbers if n % 2 == 0]


result = get_only_even([1, 2, 2, 6, 8, 12, 11, 3])
print(result)
