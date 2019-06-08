#!/usr/bin/env python3.7
def string(a):
    reverse=''
    total_len = len(a)
    for i in range(1,total_len + 1):
        reverse += a[total_len - i]
    print(reverse)

string('naveen')