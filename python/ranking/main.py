if __name__ == '__main__':
    ranked = [100, 90, 90, 80, 75, 60]
    player = [50, 65, 77, 90, 102]

    ranked = sorted(set(ranked))
    result = []
    print(ranked)    
    i = 0
    for playerScore in player:
       
        while i < len(ranked) and ranked[i] <= playerScore:
            i += 1
        result.append(len(ranked) - i + 1)

    print(result)




# 6
# 5
# 4
# 2
# 1