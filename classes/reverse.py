#!/usr/bin/env python3.7
class Reverse:
    def __init__(self,revstring):
        self.revstring = revstring
    
    def reverse(self):
        reverseStr = ''
        totalLength = len(self.revstring)
       # print(totalLength)
        for i in range(totalLength -1 ,-1,-1):
            reverseStr += self.revstring[i] 
        print(reverseStr)

rev=Reverse('ambulance')
rev.reverse()