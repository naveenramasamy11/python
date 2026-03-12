#!/usr/bin/env python3
"""Find all numbers between 1500 and 2700 divisible by both 7 and 5."""

result = [x for x in range(1500, 2701) if x % 7 == 0 and x % 5 == 0]
print(result)
