# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:30:11 2018

@author: user
"""

import os

def key_DESCR_data(dataset):
    print(dataset.keys)
    print(dataset.DESCR)
    print(dataset.data)
    
def clearscreen():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
        
def createtuple(list1):
    return tuple(list1[i] for i in list1)
    
def linenumberlist(*args):
    linenumbers=[]    
    for linenumber in args:
        linenumbers.append(linenumber)
    return linenumbers

def writetoCSV(filename,arr,*args):
    
    arrshape=arr.shape
    nrows=arrshape[0]
    ncols=arrshape[1]
    
    if args:
        with open(filename,'a+') as f:
            for linenumber in args:
                for row in range(0,nrows):
                    if row==linenumber:
                        for col in range(0,ncols):    
                            f.write("%s " % arr[row][col])
                #rewrite this to consolidate all rows in a list 1st, then write list elements into csv

def writetoCSV2(filename,arr,*args):

    lineholder = []    
    holder=[]
    
    if args:
        for lineschosen in args:
            lineholder.append(lineschosen)
#        print("lineholder contains ",lineholder) #debug
        for i in lineholder:
            holder.append(arr[i][:])
#        print("holder contains ",holder) #debug
        with open(filename,'a+') as f:
            for linestowrite in range(0,len(holder)-1):
                f.write("%s \n" % holder[linestowrite])
#                f.write("linestowrite is now %d \n" % linestowrite)
                
def writetoCSV3(filename,arr,*args):
    
    arrshape=arr.shape
    nrows=arrshape[0]
#    ncols=arrshape[1]
    
    if args:
        with open(filename,'a+') as f:
            for linenumber in args:
                f.write("%s " % arr[linenumber][:])
                #rewrite this to consolidate all rows in a list 1st, then write list elements into csv

def writetoCSVNested(filename,arr): #nested function call to function returning linenumbers
    
    arrshape=arr.shape
    nrows=arrshape[0]
    ncols=arrshape[1]
    
    linenumbers=linenumberlist(1,4,6)
    print("linenumbers are ",linenumbers)    
    
    with open(filename) as f:
        
        numbers=0        
        
        for line in f:
            if numbers in linenumbers:
                f.write(arr[numbers][:])
            numbers+=1
#            for numbers in linenumbers:                
#                if line==numbers:
#                    f.write(arr[line][:])
                        

def pick3lines(l1,l2,l3):
    
    list1=[]
    list1.append(1)
    list1.append(2)
    list1.append(3)
    
    with open('boston_data2.csv') as f:
        
        i=0
        print("3 lines chosen:\n")
        
        for line in f:
            if i in list1:
                print(line)
            i+=1
            
def pickXlines(list1):
    
    print("%d lines are \n" % len(list1))
    
    with open('boston_data2.csv') as f:
        
        i=0
        
        for line in f:
            if i in list1:
                print(line)
            i+=1

def picklines(*args): #https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3
    for k in args:
        print("%d "% k)

def pickYlines(list1):
    
    print("%d lines are \n" % len(list1))
    
    with open('boston_data2.csv') as f:
        
        for line in f:
            print(line) #debug
            for k in (0,len(list1)-1):
                print(k) #debug
                if k==line:
                    print(line)
#def pick3lines():
#    with open('boston_data2.csv') as f:
#        for k,line in f:
#            if k==1:
#                print(line)
#            if k==2:
#                print(line)
#            if k==3:
#                print(line)

#def readfile(linenumbers=[],*args): #*args => variable no. of args
#    lines = 
#    for i in linenumbers:
#        if i==linenumbers[0]:
            
        