#!/usr/bin/env python3.7
def max(x,y,z):
    if (x > y) and (x > z):
        print("Maxminum value is X:",x)
    elif(y > x) and (y > z):
        print("Maximum value is Y:",y)
    else:
        print("Maximum value is Z",z)

max(2,14,5)