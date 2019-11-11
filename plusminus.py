#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos,neg,zer=0,0,0
    
    for i in range(0,len(arr)):
        if arr[i]>0:
            pos+=1 
            
        if arr[i]<0:
            neg+=1
            
        if arr[i]==0:    
            zer+=1
            
    pos=float(pos)/len(arr)
    
    neg=float(neg)/len(arr)
    
    zer=float(zer)/len(arr)
    
    print(pos)
    print(neg)
    print(zer)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
