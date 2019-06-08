#!/usr/bin/env python3.7
def getonlyeven(even):
    newList=[]
    for i in range(len(even)):
        if even[i] % 2 == 0:
            newList.append(even[i])
    print(newList)

getonlyeven([1,2,2,6,8,12,11,3])