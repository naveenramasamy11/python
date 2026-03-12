#!/usr/bin/env python3
"""Demonstrates relational (comparison) operators."""

a = 20
response = int(input("Enter a number: "))

if response < a:
    print(f"{response} is less than {a}")
elif response > a:
    print(f"{response} is greater than {a}")
else:
    print(f"{response} is equal to {a}")
