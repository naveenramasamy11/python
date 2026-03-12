#!/usr/bin/env python3
"""Right-aligned growing star pattern."""

n = int(input("Enter the number of lines: "))
for i in range(1, n):
    print(" " * (n - i) + "* " * i)
