#!/usr/bin/env python3
"""Print numbers in a range, skipping 0 and 3."""

n = int(input("Enter a number: "))
result = [i for i in range(n) if i not in (0, 3)]
print(*result)
