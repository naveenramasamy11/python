#!/usr/bin/env python3
"""Number guessing game — guess a single-digit number (0-9)."""

while True:
    x = input("Guess a single-digit number (0-9): ").strip()
    if x.isdigit() and 0 <= int(x) <= 9:
        print("You guessed it right!")
        break
    print("Try again — enter a number between 0 and 9.")
