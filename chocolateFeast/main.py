def chocolateFeast(n, c, m):
    # Write your code here
    total = n // c
    wrappers = total
    while wrappers >= m:
        aux = wrappers // m
        wrappers = (wrappers % m) + aux
        total += aux

    return total

if __name__ == "__main__":
    n = 10
    c = 2
    m = 5   
    result = chocolateFeast(n, c, m)
    print(result)

    