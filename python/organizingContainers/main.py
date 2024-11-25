import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#


def organizingContainers(container):
    # Write your code here
    col_capacity = []
    sum_balls = []
    for i in range(len(container)):
        col_capacity.append(sum(container[i]))
        aux = 0
        for j in range(len(container[i])):
            aux += container[j][i]
        sum_balls.append(aux)

    if sorted(col_capacity) == sorted(sum_balls):
        return "Possible"

    return "Impossible"


if __name__ == "__main__":

    container_1 = [[1, 1], [1, 1]]  # Possible
    container_2 = [[0, 2], [1, 1]]  # Impossible

    container_3 = [[1, 3, 1], [2, 1, 2], [3, 3, 3]]  # Impossible

    # [6,7,6] soma das quantidades de cada tipo de bola
    # [5,5,9] soma da capacidade de cada container

    container_4 = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]  # Possible

    organizingContainers(container_1)
    organizingContainers(container_2)
    organizingContainers(container_4)
    organizingContainers(container_3)
