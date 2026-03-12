#!/usr/bin/env python3
"""Calculate factorial of n using a loop."""

n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
