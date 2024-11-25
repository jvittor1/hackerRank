def extraLongFactorials(n):
    # Write your code here
    if n == 0:
        return 1
    
    result = 1
    while n > 1:
        result = result * n
        n = n - 1

    return result
if __name__ == '__main__':
    n = 25

    print(extraLongFactorials(n))
