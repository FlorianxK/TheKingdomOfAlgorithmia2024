from typing import *

def dayTen():
    arr = []
    rowVal = {}
    #read
    with open("Day10/10_1.txt") as file:
        for i,line in enumerate(file):
            line = line.strip()
            arr.append(list(line))
            if '*' in line:
                continue

            x = line.replace(".","")
            rowVal[i] = x

    colVal = {}
    for i,col in enumerate(zip(*arr)):
        if '*' in col:
            continue

        x = "".join(col).replace(".","")
        colVal[i] = x

    word = ""
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '.':
                row = rowVal[i]
                col = colVal[j]
                for c in row:
                    if c in col:
                        arr[i][j] = c
                        word += c
                        break
    return word

def dayTen2():
    total = 0
    alphabet = {}
    val = 1
    for i in range(65,65+26):
        alphabet[chr(i)] = val
        val += 1
    
    def calc(arr):
        rowVal = {}
        for i,row in enumerate(arr):
            if '*' in row:
                continue

            x = "".join(row).replace(".","")
            rowVal[i] = x

        colVal = {}
        for i,col in enumerate(zip(*arr)):
            if '*' in col:
                continue

            x = "".join(col).replace(".","")
            colVal[i] = x

        word = ""
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if arr[i][j] == '.':
                    row = rowVal[i]
                    col = colVal[j]
                    for c in row:
                        if c in col:
                            arr[i][j] = c
                            word += c
                            break
        
        res = 0
        for i in range(len(word)):
            res += (i+1)*alphabet[word[i]]
        return res

    with open("Day10/10_2.txt") as file:
        blocks = file.read().split("\n\n")

    for b in blocks:
        lines = b.splitlines()
        j = 0
        for _ in range(15):
            arr = []
            for l in lines:
                arr.append(list(l[j:j+8]))
            v = calc(arr)
            total += v
            
            j += 9
    return total

def dayTen3():
    pass

def main():
    print("Hallo")
    print(dayTen(), "ist die Lösung von Teil 1")
    print(dayTen2(), "ist die Lösung von Teil 2")
    print(dayTen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()