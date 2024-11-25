def surfaceArea(a):
    # Write your code here
    n = len(a)
    m = len(a[0])
    area = 2*n*m
    for i in range(n):
        for j in range(m):
            if i == 0:
                area += a[i][j]
            else:
                area += abs(a[i][j] - a[i-1][j])
            if i == n-1:
                area += a[i][j]
            if j == 0:
                area += a[i][j]
            else:
                area += abs(a[i][j] - a[i][j-1])
            if j == m-1:
                area += a[i][j]

    return area




if __name__ == '__main__':
    matrix = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]
    print(surfaceArea(matrix))

    