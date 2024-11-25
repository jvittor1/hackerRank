def getMinimumCost(array, magicSquare):
    minimumCost = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            minimumCost += abs(array[i][j] - magicSquare[i][j])
    return minimumCost


def is_magic_square(s):
    # all options
    options = [
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    ]
    
    # get minimum cost
    minimumCost = 9999
    for option in options:
        minimumCost = min(minimumCost, getMinimumCost(s, option))
    return minimumCost

    

if __name__ == '__main__':

    s = [

        [4, 8, 2], # 15 14 1
        [4, 5, 7], # 15 16 -1
        [6, 1, 6]  # 15 13 2
        
        ]
    
     # tem que ser 4
    

    #    [8, 3, 4], # 15 15
    #    [1, 5, 9], # 15 15 
    #    [6, 7, 2]  # 15 15


        
    
        
            


    magic_square = is_magic_square(s)
    print(magic_square)