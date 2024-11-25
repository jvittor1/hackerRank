def biggerWords(word):
    value = len(word) - 1
    
    value = len(word) - 2
    while value >= 0 and word[value] >= word[value + 1]:
        value -= 1
    
    if value == -1:
        return 'no answer'
    
    
    switchPosition = len(word) - 1
    while switchPosition >= value  and word[switchPosition] <= word[value]:
        switchPosition -= 1
 

    # switch positions
    word = list(word)
    word[value], word[switchPosition] = word[switchPosition], word[value]
    word = ''.join(word)
    word = word[:value + 1] + word[value + 1:][::-1]

    return word

if __name__ == "__main__":
    n = ['dcbb', 'dcba', 'hefg', 'dhck', 'dkhc', 'lmon', 'fedcbabcd']
    a = ['dcbb', 'dcba']

    for item  in n:
        # biggerWords(item)
        print(biggerWords(item))


    # dcbb
    # 3211