#!/usr/bin/env python3.7
squareValueofitself=list()
def square(n):
    for i in range(1,n+1):
        squareValueofitself.append(i * i)
    print(squareValueofitself)
square(10)
