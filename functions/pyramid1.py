#!/usr/bin/env python3.7
def pyramid(n):
    a = ' '
    b = '* '
    for i in range(n):
      print((n -i) * a, end='')
      print(i * b)

    for i in range(n,-1,-1):
      print((n -i) * a, end='')
      print(i * b)

pyramid(4)