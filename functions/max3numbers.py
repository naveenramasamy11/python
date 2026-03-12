#!/usr/bin/env python3
"""Find the maximum of three numbers."""


def max_of_three(x: float, y: float, z: float) -> float:
    return max(x, y, z)


result = max_of_three(2, 14, 5)
print(f"Maximum value: {result}")
