#!/usr/bin/env python3
"""Demonstrates common Python list operations."""

li = [1, 2, 3, 4, 5]

print("Using list() constructor:")
a = list((1, 2, 3, 4))
print(a)
print(li)

print("\nChange item value:")
a[0] = 0
print(a)

print("\nList length using len():")
print(len(a))

print("\nAppend:")
a.append(5)
print(a)

print("\nInsert at index 0:")
a.insert(0, 1)
print(a)

print("\nRemove value 0:")
a.remove(0)
print(a)
