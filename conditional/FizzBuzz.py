#!/usr/bin/env python3.7
n=50
for i in range(n):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
    continue
  elif i % 3 == 0:
    print("Fuzz")
    continue
  elif i % 5 == 0:
    print("Buzz")
    continue
