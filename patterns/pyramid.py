#!/usr/bin/env python3.7
def pyramid(x):
    for i in range(x):
        for k in range(x-i,-1,-1):
            print(' ',end='')
        for j in range(1,i+1):
            print('* ',end='')
        print('')
    for i in range(x):
        for k in range(i+1):
            print(' ',end='')
        for j in range(x-i-1,-1,-1):
            print('* ',end='')
        print('')

pyramid(10)
