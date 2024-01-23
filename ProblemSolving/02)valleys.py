#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    curr = 0
    for i in range(0, steps):
        if (path[i]== "U"):
            curr +=1
        else:
            curr -=1
        if (curr==0 and i>0):
            if (path[i]=="U"):
                valleys+=1
        #print(i, curr, valleys)
    
    return valleys
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
