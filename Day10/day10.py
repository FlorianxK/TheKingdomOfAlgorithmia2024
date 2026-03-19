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
    # vielleicht bricht zu früh ab und muss mehrmals checken ob ein arr lösbar ist? falls sich was geändert hat
    alphabet = {}
    val = 1
    for i in range(65,65+26):
        alphabet[chr(i)] = val
        val += 1

    def fillArr(arr):
        res = 0
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
        
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if arr[i][j] == '.':
                    row = rowVal[i]
                    col = colVal[j]
                    for c in row:
                        if c == '?':
                            continue
                        if c in col:
                            arr[i][j] = c
                            break

        for i in range(n):
            for j in range(n):
                if arr[i][j] == '.':
                    setRow = set()
                    setCol = set()
                    for k in range(n):
                        if arr[i][k] in setRow:
                            setRow.remove( arr[i][k] )
                        else:
                            setRow.add( arr[i][k] )
                        if arr[k][j] in setCol:
                            setCol.remove( arr[k][j] )
                        else:
                            setCol.add( arr[k][j] )
                        
                        if arr[i][k] == '?':
                            qm = (i,k)
                        elif arr[k][j] == '?':
                            qm = (k,j)

                    solo = setRow^setCol
                    if '?' in solo:
                        solo.remove('?')
                    if len(solo) == 1:
                        # found
                        letter = ''.join(solo)
                        arr[i][j] = letter
                        a,b = qm
                        arr[a][b] = letter

        # find word
        word = ""
        for i in range(2,n-2):
            for j in range(2,n-2):
                if arr[i][j] == '.':
                    return 0
                word += arr[i][j]
        print(word)
        res = 0
        for i in range(len(word)):
            res += (i+1)*alphabet[word[i]]

        return res

    res = 0
    fullArr = []
    nextArr = []
    counter = 0
    with open("Day10/10.txt") as file:
        for line in file:
            counter += 1
            line = list(line.strip())
            fullArr.append(line)
            if counter >= 7:
                nextArr.append(line)

            if counter == 8:
                counter = 2
                # work
                index = 0
                while index+8 <= len(fullArr[0]):
                    arr = []
                    for l in fullArr:
                        arr.append( l[index:index+8] )
                    index += 6
                    
                    # FULL ARR FOUND
                    res += fillArr(arr)

                #after work
                fullArr = nextArr
                nextArr = []
    return res

def main():
    print("Hallo")
    #print(dayTen(), "ist die Lösung von Teil 1")
    #print(dayTen2(), "ist die Lösung von Teil 2")
    print(dayTen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()