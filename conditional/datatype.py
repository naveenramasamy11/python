#!/usr/bin/env python3
"""Demonstrates Python built-in data types using type()."""

data = [1452, 11.23, 1 + 2j, True, "w3resource", (0, -1), [5, 12], {"class": "V", "section": "A"}]

for item in data:
    print(f"Value: {str(item):<35} | Type: {type(item).__name__}")
