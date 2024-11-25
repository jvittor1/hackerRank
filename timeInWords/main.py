import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#


def getTime(h):
    time = {
        1: "one",2: "two",3: "three",4: "four",5: "five",6: "six",7: "seven",8: "eight",9: "nine",10: "ten",
        11: "eleven",12: "twelve",13: "thirteen",14: "fourteen",15: "fifteen",16: "sixteen",17: "seventeen",18: "eighteen",19: "nineteen",20: "twenty",
        21: "twenty one",22: "twenty two",23: "twenty three",24: "twenty four",25: "twenty five",26: "twenty six",27: "twenty seven",28: "twenty eight",
        29: "twenty nine"
    }

    return time[h]


def timeInWords(h, m):
    if m == 0:
        return getTime(h) + " o' clock"

    elif m >= 1 and m < 30:
        if m == 1:
            return "one minute past " + getTime(h)
        elif m == 15:
            return "quarter past " + getTime(h)
        else:
            return getTime(m) + " minutes past " + getTime(h)

    elif m == 30:
        return "half past " + getTime(h)

    elif m > 30 and m < 60:
        if m == 45:
            return "quarter to " + getTime(h + 1)
        else:
            return getTime(60 - m) + " minutes to " + getTime(h + 1)


if __name__ == "__main__":
    h = 7
    m = 15
    result = timeInWords(h, m)
    print(result)
