#!/usr/bin/env python3.7
class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def calc(self):
        return self.l * self.b

abj=Rectangle(4,3)
print("Area of length and breath is:\n", abj.calc())
