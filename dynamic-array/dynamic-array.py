#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    seqList, results = [], []
    lastAnswer = 0
    for i in range(n):
        seqList.append([])
    for q in queries:
        seq = ((q[1] ^ lastAnswer)%n)
        if q[0] == 1:
            seqList[seq].append(q[2])
        elif q[0] == 2:
            lastAnswer = seqList[seq][q[2] % len(seqList[seq])]
            print(lastAnswer)
            results.append(lastAnswer)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
