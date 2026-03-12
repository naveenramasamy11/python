#!/usr/bin/env python3
"""Check if a string is a palindrome."""


def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


for word in ("madam", "naveen", "racecar", "hello"):
    result = "Yes, palindrome" if is_palindrome(word) else "No, not a palindrome"
    print(f"{word!r}: {result}")
