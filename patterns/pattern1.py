#!/usr/bin/env python3
"""Right-aligned pyramid — centered star triangle."""

n = int(input("Enter the number of lines for pyramid: "))
for i in range(1, n):
    print(" " * (n - i) + "* " * i)
