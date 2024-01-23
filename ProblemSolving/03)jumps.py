#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    ans = 0
    n = len(c)
    if(n<=2):
        return 1
        
    idx= 0
    while(idx<n-1):
    
        if(idx+2<n):
            if(c[idx+2]!=1):
                ans+= 1
                idx += 2
            elif(c[idx+1]!=1):
                ans += 1
                idx += 1
        elif(idx+1<n):
            if(c[idx+1]!=1):
                ans += 1
                idx += 1
    return ans
        
            
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
