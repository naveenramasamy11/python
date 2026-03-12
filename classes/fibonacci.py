#!/usr/bin/env python3
"""Fibonacci sequence using a class."""


class Fibonacci:
    def __init__(self, fn: int, sn: int) -> None:
        self.fn = fn
        self.sn = sn

    def fib(self, n: int) -> None:
        for _ in range(n):
            print(self.fn)
            self.fn, self.sn = self.sn, self.fn + self.sn


obj = Fibonacci(1, 1)
obj.fib(10)
