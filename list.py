#!/usr/bin/env python3.7
li=[1,2,3,4,5]
print("using list method")
a=list((1,2,3,4))
print(a)
print(li)

print("Change Item Value")
a[0]=0
print(a)

print("file lenghth using len method")
tmp=len(a)
print(tmp)

print("Append")
a.append(5)
print(a)

print("Insert")
a.insert(0,1)
print(a)

print("Remove")
a.del(0)
print(a)
