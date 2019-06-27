#!/usr/bin/env python3.7
class Fibonacci:
    def __init__(self,fn,sn):
        self.fn = fn 
        self.sn= sn 

    def fib(self,n):
        i = 0
        while i < n:
            thirdNumber = self.fn + self.sn
            print(self.fn)
            self.fn = self.sn
            self.sn = thirdNumber
            i += 1
abj1 = Fibonacci(1,1)
abj1.fib(10)

