#!/usr/bin/env python3
"""Demonstrates a while loop with a break condition."""

a = 10
while True:
    response = int(input("Enter a number divisible by 10: "))
    if response % a == 0:
        print(f"{response} is divisible by {a}")
        break
    print("Try again.")
