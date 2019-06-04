#!/usr/bin/env python3.7
def calc(a,b):
  if (type(a) == int,float) and (type(b) == int,float):
    print("addition of ",a,"and",b,"is: ",a + b)
    print("subtraction of ",a,"and",b,"is: ",a + b)
    print("divison of ",a,"and",b,"is: ", a + b)
    print("multiplication of ",a,"and",b,"is: ", a + b)
  else:
    print("enter numbers")

calc("test","test1")
