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
    alphabet = {}
    val = 1
    for i in range(65,65+26):
        alphabet[chr(i)] = val
        val += 1

    def calc(arr):
        m,n = len(arr),len(arr[0])

        def solve_block(top,left):
            def get(i,j):
                return arr[top+i][left+j]

            def setv(i,j,val):
                if arr[top+i][left+j] != val:
                    arr[top+i][left+j] = val
                    return True
                return False

            changed = False
            for i in range(8):
                row = [get(i,j) for j in range(8)]
                if '*' in row:
                    continue

                row_str = "".join(row).replace(".","")
                for j in range(8):
                    if get(i,j) != '.':
                        continue

                    col = [get(x,j) for x in range(8)]
                    if '*' in col:
                        continue

                    col_str = "".join(col).replace(".","")
                    for c in row_str:
                        if c != '?' and c in col_str:
                            changed = setv(i,j,c) or changed
                            break

            for i in range(8):
                for j in range(8):
                    if get(i,j) != '.':
                        continue

                    setRow = set()
                    setCol = set()
                    qm = []

                    for k in range(8):
                        a = get(i,k)
                        b = get(k,j)

                        if a in setRow:
                            setRow.remove(a)
                        else:
                            setRow.add(a)

                        if b in setCol:
                            setCol.remove(b)
                        else:
                            setCol.add(b)

                        if a == '?':
                            qm.append((i,k))
                        if b == '?':
                            qm.append((k,j))

                    solo = setRow ^ setCol
                    solo.discard('?')

                    if len(solo) == 1:
                        letter = next(iter(solo))
                        changed = setv(i,j,letter) or changed
                        for x,y in qm:
                            changed = setv(x,y,letter) or changed
            return changed

        def get_word(top,left):
            word = ""
            for i in range(2,6):
                for j in range(2,6):
                    c = arr[top+i][left+j]
                    if c == '.':
                        return 0
                    word += c
            return sum((i+1)*alphabet[c] for i,c in enumerate(word))

        changed = True
        while changed:
            changed = False
            for i in range(0, m-7, 6):
                for j in range(0, n-7, 6):
                    if solve_block(i,j):
                        changed = True
        res = 0
        for i in range(0, m-7, 6):
            for j in range(0, n-7, 6):
                res += get_word(i,j)
        return res

    arr = []
    with open("Day10/10_3.txt") as file:
        for line in file:
            arr.append(list(line.strip()))

    return calc(arr)

def main():
    print("Hallo")
    print(dayTen(), "ist die Lösung von Teil 1")
    print(dayTen2(), "ist die Lösung von Teil 2")
    print(dayTen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()