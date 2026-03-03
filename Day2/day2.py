from typing import *

def dayTwo():
    res = 0
    #read
    with open("Day2/2_1.txt") as file:
        words = file.readline().strip().split(':')[1].split(',')
        next(file)
        arr = file.readline().strip().split()
    for a in arr:
        for w in words:
            if w in a:
                res += 1
    return res

def dayTwo2():
    res = 0
    #read
    with open("Day2/2_2.txt") as file:
        words = file.readline().strip().split(':')[1].split(',')
        next(file)
        arr = file.readlines()

    for line in arr:
        runes = line.strip().split()
        lineCount = 0
        for rune in runes:
            bits = [0]*len(rune)
            revRune = rune[::-1]
            for w in words:
                pos = []
                start = 0
                # l to r
                while True:
                    start = rune.find(w,start)
                    if start == -1:
                        break
                    pos.append(start)
                    start += len(w)
                
                for p in pos:
                    for i in range(p,len(w)+p):
                            bits[i] = 1

                pos = []
                start = 0
                # r to l
                while True:
                    start = revRune.find(w,start)
                    if start == -1:
                        break
                    pos.append(start)
                    start += len(w)

                for p in pos:
                    originalStart = len(rune)-p-len(w)
                    for i in range(originalStart,originalStart+len(w)):
                        bits[i] = 1

            lineCount += sum(bits)
        res += lineCount

    return res

def dayTwo3():
    arr = []
    #read
    with open("Day2/2_3.txt") as file:
        words = file.readline().strip().split(':')[1].split(',')
        next(file)
        for line in file:
            arr.append(line.strip())
    m,n = len(arr),len(arr[0])
    bits = [[0]*n for _ in range(m)]

    #l to r
    for i,row in enumerate(arr):
        row = row*2
        for w in words:
            pos = []
            start = 0
            while True:
                start = row.find(w,start)
                if start == -1:
                    break
                pos.append(start)
                start += len(w)
            
            for p in pos:
                if p < n:
                    for k in range(p,p+len(w)):
                        bits[i][k%n] = 1
    
    #r to l
    for i,row in enumerate(arr):
        revRow = row[::-1]*2
        for w in words:
            pos = []
            start = 0
            while True:
                start = revRow.find(w,start)
                if start == -1:
                    break
                pos.append(start)
                start += len(w)

            for p in pos:
                if p < n:
                    originalStart = len(revRow)-p-len(w)
                    for k in range(originalStart,originalStart+len(w)):
                        bits[i][k%n] = 1
    
    #t to b
    for j,col in enumerate(zip(*arr)):
        col = ''.join(col)
        for w in words:
            pos = []
            start = 0
            while True:
                start = col.find(w,start)
                if start == -1:
                    break
                pos.append(start)
                start += len(w)
            
            for p in pos:
                if p < m:
                    for k in range(p,p+len(w)):
                        bits[k%m][j] = 1

    #b to t
    for j,col in enumerate(zip(*arr)):
        col = ''.join(col)
        col = col[::-1]
        for w in words:
            pos = []
            start = 0
            while True:
                start = col.find(w,start)
                if start == -1:
                    break
                pos.append(start)
                start += len(w)

            for p in pos:
                if p < m:
                    originalStart = len(col)-p-len(w)
                    for k in range(originalStart,originalStart+len(w)):
                        bits[k%m][j] = 1
    res = 0
    for b in bits:
        res += sum(b)
    return res

def main():
    print("Hallo")
    print(dayTwo(), "ist die Lösung von Teil 1")
    print(dayTwo2(), "ist die Lösung von Teil 2")
    print(dayTwo3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()