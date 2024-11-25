import math

def encryption(s):
    noSpaceString = s.replace(" ", "")
    stringLength = len(noSpaceString)
    rows = math.floor(math.sqrt(stringLength))
    columns = math.ceil(math.sqrt(stringLength))
    if rows * columns < stringLength:
        rows += 1
    result = ""
    for i in range(columns):
        for j in range(rows):
            if i + j * columns < stringLength:
                result += noSpaceString[i + j * columns]
        result += " "
    
    return result

if __name__ == '__main__':
    s = "haveaniceday"
    result = encryption(s)
    print(result)

    
    # 11

    # 3 4
    # have
    # anic
    # eday

    # hae
    # and
    # via 
    # ecy

