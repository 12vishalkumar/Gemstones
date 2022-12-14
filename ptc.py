import math
import os
import random
import re
import sys
from string import ascii_lowercase
# Complete the 'gemstones' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
def gemstones(arr):
    # Write your code here
    ch = ascii_lowercase
    ct = 0
    for i in ch:
        pst = True
        for s in arr:
            if i not in s:
                pst = False
        if pst:
            ct += 1
    return ct 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    fptr.write(str(result) + '\n')
    fptr.close()