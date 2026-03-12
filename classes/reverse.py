#!/usr/bin/env python3
"""String reversal using a class."""


class Reverse:
    def __init__(self, text: str) -> None:
        self.text = text

    def reverse(self) -> str:
        return self.text[::-1]


for word in ("ambulance", "camera", "photography", "mars"):
    obj = Reverse(word)
    print(f"{word} -> {obj.reverse()}")
