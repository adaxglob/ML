# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 13:04:33 2018

@author: user
"""

import helper

list1=[]
for i in range(0,10):
    list1.append(i)
    
newtuple=helper.createtuple(list1)
print(newtuple)

#with open('boston_data2.csv') as f:
#    filedata=f.read()
#    print(filedata)
    
with open('boston_data2.csv') as f:
    for i,line in enumerate(f):
        if i==5:
            print(line)
        if i==25:
            print(line)
            
helper.pick3lines(1,2,3)

list2=[1,7,8,9,21,24]
helper.pickXlines(list2)
helper.picklines(8,8,6,4)
#helper.pickYlines(list2)