#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    #
    # Write your code here.
    #
    a=0
    b=0
    arr.sort()
    for i in range(0,4):
        a+=arr[i]
    for j in range(1,5):
        b+=arr[j]
    print("{0} {1}".format(a,b))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
