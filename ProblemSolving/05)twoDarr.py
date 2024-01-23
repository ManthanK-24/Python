#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    ans = -1000
    #print(arr)
    for i in range(1, 5):
        for j in range(1, 5):
            val = arr[i][j]
            val += arr[i-1][j] + arr[i+1][j]
            val += arr[i-1][j-1] + arr[i-1][j+1]
            val += arr[i+1][j-1] + arr[i+1][j+1]
            if (val>ans):
                ans = val
            
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
