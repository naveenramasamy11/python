#!/usr/bin/env python3.7
r1=[]
for x in range(1500,2701):
  if (x % 7 == 0) and (x % 5 == 0):
    r1.append(x)
print(r1)


