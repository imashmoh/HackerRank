# Problem :
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with 6 places after the decimal.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    # Write your code here
    countZero = 0
    countPositive = 0
    countNegative = 0
    n = len(arr)
    for i in arr:
        if i > 0:
            countPositive += 1
        elif i < 0:
            countNegative += 1
        else:
            countZero += 1
    print("{:.6f}".format(countPositive/n))
    print("{:.6f}".format(countNegative/n))
    print("{:.6f}".format(countZero/n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(arr)
