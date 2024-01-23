#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def mod(num, a):
    res = 0
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % a
    return res

def repeatedString(s, n):
    # Write your code here
    ans = 0
    sz = len(s)
    times = s.count('a', 0, sz)
    # times = 0
    # for i in range(0,sz):
    #     if (s[i]=='a'):
    #         times+=1
    
    #below line of code is tricky
    ans = math.floor((n/sz))*times
    
    #till = mod(str(n), sz)
    till = n % sz
    
    for i in range(0, till):
        if (s[i]=='a'):
            ans+=1
    #print(sz, times, ans, till)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
