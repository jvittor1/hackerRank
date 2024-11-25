import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#


def larrysArray(A):
    # Write your code here
    n = len(A)
    s = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                s += 1

    return "YES" if s % 2 == 0 else "NO"


if __name__ == "__main__":
    a = [3, 1, 2]

    b = [1, 3, 4, 2]

    # 1 3 4 2
    #

    c = [1, 2, 3, 5, 4]

    # Array 1
    array1 = [
        22,
        16,
        6,
        7,
        24,
        8,
        11,
        26,
        18,
        17,
        10,
        4,
        1,
        23,
        15,
        20,
        21,
        14,
        25,
        2,
        3,
        9,
        13,
        28,
        12,
        19,
        5,
        27,
    ]

    # Array 2
    array2 = [7, 10, 9, 4, 6, 11, 3, 2, 8, 1, 5]

    # Array 3
    array3 = [7, 19, 9, 10, 2, 3, 6, 1, 18, 15, 14, 8, 4, 11, 17, 16, 5, 13, 12]

    # Array 4
    array4 = [13, 11, 17, 5, 16, 9, 7, 6, 2, 18, 15, 4, 1, 8, 14, 3, 10, 12]

    # Array 5
    array5 = [
        4,
        20,
        22,
        17,
        8,
        14,
        11,
        9,
        3,
        12,
        7,
        1,
        10,
        2,
        15,
        18,
        5,
        13,
        6,
        19,
        16,
        21,
        23,
        24,
    ]

    # Array 6
    array6 = [
        29,
        13,
        9,
        19,
        25,
        22,
        11,
        12,
        20,
        10,
        4,
        5,
        21,
        15,
        8,
        7,
        2,
        16,
        18,
        17,
        26,
        27,
        6,
        3,
        14,
        1,
        23,
        24,
        28,
    ]

    # Array 7
    array7 = [
        10,
        22,
        16,
        13,
        1,
        3,
        17,
        11,
        21,
        15,
        18,
        6,
        9,
        4,
        20,
        19,
        5,
        2,
        7,
        14,
        12,
        8,
    ]

    array8 = [17, 21, 2, 1, 16, 9, 12, 11, 6, 18, 20, 7, 14, 8, 19, 10, 3, 4, 13, 5, 15]

    g = [7, 9, 15, 8, 10, 16, 6, 14, 5, 13, 17, 12, 3, 11, 4, 1, 18, 2]

    # print(larrysArray(a))
    # print(larrysArray(b))
    # print(larrysArray(c))
    # print(larrysArray(array1))
    # print(larrysArray(array2))
    # print(larrysArray(array3))
    # print(larrysArray(array4))
    # print(larrysArray(array5))
    # print(larrysArray(array6))
    # print(larrysArray(array7))
    print(larrysArray(g))
