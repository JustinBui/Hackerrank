#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    l = [0] * n
    
    for a, b, k in queries:
        start = a - 1
        end = b - 1
        l[start] += k
        if end + 1 < n:
            l[end + 1] -= k
    
    max_ = float('-inf')
    for i in range(1, n):
        l[i] += l[i -1]        
        max_ = max(max_, l[i])
        
    return max_

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
