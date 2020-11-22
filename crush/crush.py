#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = []
    for i in range(n):
        arr.append(0)
    maxsum, x = 0, 0
    for q in queries:
        arr[q[0] - 1] += q[2]
        if q[1] <= n - 1:
            arr[q[1]] -= q[2]
    for i in arr:
        x += i
        if x > maxsum:
            maxsum = x
    return maxsum


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + "\n")

    fptr.close()
