#!/usr/bin/env python3
"""Count total odd and even numbers from 1 to n."""

n = int(input("Enter a number: "))
even = sum(1 for i in range(1, n + 1) if i % 2 == 0)
odd = n - even
print(f"Total odd:  {odd}")
print(f"Total even: {even}")
