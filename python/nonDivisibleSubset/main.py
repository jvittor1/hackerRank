import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    remainder_count = [0] * k

    for num in s:
        remainder_count[num % k] += 1

    subset_size = min(remainder_count[0], 1)

    for i in range(1, (k // 2) + 1):
        if i != k - i:
            subset_size += max(remainder_count[i], remainder_count[k - i])
        else:
            subset_size += min(remainder_count[i], 1)

    return subset_size


if __name__ == "__main__":
    s = [1, 7, 2, 4]  # 3
    k = 3

    s = [
        278,
        576,
        496,
        727,
        410,
        124,
        338,
        149,
        209,
        702,
        282,
        718,
        771,
        575,
        436,
    ]  # 11
    k = 7

    print(nonDivisibleSubset(k, s))
