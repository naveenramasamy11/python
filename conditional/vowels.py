#!/usr/bin/env python3.7
v=0
c=0
string=input("Enter a string or sentence:\n")
for i in string:
  if i.lower() in "aeiou":
    v += 1
#  else:
  elif i not in "aeiou" and i not in ' ':
    c += 1
print("total vowels", v)
print("total consonents", c)

