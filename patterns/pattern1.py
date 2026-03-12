#!/usr/bin/env python3.7
#  *
# * *
#* * *
n = int(input("Enter the number of lines you want for pyramid:"))
for i in range(1,n):
  for s in range(1,n-i):
    print(' ',end='')
  for j in range(1,i+1):
    print("* ",end='')
  print('')

