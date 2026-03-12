#!/usr/bin/env python3
"""Hourglass star pattern — expanding then shrinking rows."""

n = 5
for i in range(n):
    print("* " * i)
for i in range(n, 0, -1):
    print("* " * i)
