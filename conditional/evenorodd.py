#!/usr/bin/env python3.7
n=int(input("enter a number to find total odd and even numbers:\n"))
odd=0
even=0
if n == 1: 
  odd = 1
  print(odd)
else:
  for i in range(1,n+1):
    if i % 2 == 0:
      even += 1
    else:
      odd += 1
print("total odd:",odd)
print("total even:",even)
