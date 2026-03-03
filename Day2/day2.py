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
                    for i in range(len(revRune)-1,len(revRune)-1-len(w),-1):
                        bits[i] = 1

            lineCount += sum(bits)
        print(lineCount)
        res += lineCount

    return res

def dayTwo3():
    pass

def main():
    print("Hallo")
    #print(dayTwo(), "ist die Lösung von Teil 1")
    print(dayTwo2(), "ist die Lösung von Teil 2")
    print(dayTwo3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()