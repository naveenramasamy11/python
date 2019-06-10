#!/usr/bin/env python3.7
def isPalindome(p):
    first=''
    second=''
    position = int(len(p) / 2)
    for i in range(position):
        first += p[i]
    for j in range(len(p) -1,position,-1):
        second += p[j]
    if first == second:
        print(p,":Yes!, it is a palindrome")
    else:
        print(p,":NO!, It is not palindrome")
#    print(first,second)
isPalindome('madam')
isPalindome('naveen')