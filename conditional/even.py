#!/usr/bin/env python3
"""Print all even numbers from 0 up to n."""

n = int(input("Enter the upper limit: "))
print(f"Even numbers from 0 to {n}:")
for i in range(0, n + 1, 2):
    print(i)
