#!/usr/bin/env python3
"""Generate the first 10 Fibonacci numbers."""

a, b = 0, 1
for _ in range(10):
    a, b = b, a + b
    print(a)
