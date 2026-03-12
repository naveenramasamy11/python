#!/usr/bin/env python3
"""Rectangle area calculation using a class."""


class Rectangle:
    def __init__(self, length: float, breadth: float) -> None:
        self.length = length
        self.breadth = breadth

    def area(self) -> float:
        return self.length * self.breadth


obj = Rectangle(4, 3)
print(f"Area of rectangle (length={obj.length}, breadth={obj.breadth}): {obj.area()}")
