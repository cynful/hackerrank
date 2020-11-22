#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    largest = -sys.maxsize
    for y, row in enumerate(arr[:-2]):
        for x, e in enumerate(row[:-2]):
            i = (
                arr[y][x]
                + arr[y][x + 1]
                + arr[y][x + 2]
                + arr[y + 1][x + 1]
                + arr[y + 2][x]
                + arr[y + 2][x + 1]
                + arr[y + 2][x + 2]
            )
            if i > largest:
                largest = i
    return largest


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
