#!/usr/bin/env python3.7
class Pyramid:
    def __init__(self,Range,pattern,spaces):
        self.Range = Range
        self.pattern = pattern
        self. spaces = spaces

    def convert(self):
        n = self.Range
        for i in range(n):
            print((n - i) * self.spaces, end='')
            print(i * self.pattern)
        for i in range(n,-1,-1):
            print((n - i) * self.spaces, end = '')
            print(i * self.pattern)
abj1 = Pyramid(10,' *',' ')
abj1.convert()