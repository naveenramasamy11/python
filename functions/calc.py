#!/usr/bin/env python3
"""Basic calculator function with type validation.

Bug fix: original script used addition (+) for all four operations.
"""


def calc(a: float, b: float) -> None:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        print("Error: both arguments must be numbers.")
        return
    print(f"Addition:       {a} + {b} = {a + b}")
    print(f"Subtraction:    {a} - {b} = {a - b}")
    print(f"Multiplication: {a} x {b} = {a * b}")
    if b != 0:
        print(f"Division:       {a} / {b} = {a / b:.4f}")
    else:
        print("Division:       undefined (division by zero)")


calc(10, 3)
calc("test", "test1")
