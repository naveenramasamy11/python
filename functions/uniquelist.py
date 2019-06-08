#!/usr/bin/env python3.7
def unique(uniquelist):
    new_list=[]
    for i in range(len(uniquelist)):
        if uniquelist[i] not in new_list:
            new_list.append(uniquelist[i])
    print(new_list)

unique([1,2,3,4,4,5,5,6,7,7,7,7,7,8,8,8,8])
     
