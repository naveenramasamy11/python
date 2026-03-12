#!/usr/bin/env python3
"""Count vowels and consonants in a string."""

string = input("Enter a string or sentence: ").lower()
vowels = sum(1 for ch in string if ch in "aeiou")
consonants = sum(1 for ch in string if ch.isalpha() and ch not in "aeiou")
print(f"Total vowels:     {vowels}")
print(f"Total consonants: {consonants}")
