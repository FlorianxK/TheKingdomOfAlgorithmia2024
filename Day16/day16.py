from collections import defaultdict
from typing import *

def daySixteen():
    arr = []
    #read
    with open("Day16/16_1.txt") as file:
        spin = [int(x) for x in file.readline().strip().split(',')]
        for line in file:
            if line != '\n':
                arr.append(line.rstrip())

    slotRows = defaultdict(list)
    for i in range(len(arr)):
        cat = ""
        index = 1
        for j in range(len(arr[i])):
            
            if arr[i][j] == ' ' and len(cat) == 3:
                cat = cat.strip()
                if cat:
                    slotRows[index].append(cat)
                index += 1
                cat = ""
            else:
                cat += arr[i][j]
        
        cat = cat.strip()
        if cat:
            slotRows[index].append(cat)

    indices = [0]*len(slotRows)

    def oneRound(num):
        symbols = []
        c = Counter()
        for i in range(len(spin)):
            v = slotRows[i+1]
            indices[i] = (indices[i]+spin[i])%len(v)
            val = v[ indices[i] ]
            symbols.append(val)
            cat = Counter(val)
            c = c+cat
        
        coins = 0
        for v in c.values():
            if v >= 3:
                coins += 1
                coins += v-3
        return symbols,coins
    
    res = 0
    rounds = 100
    for k in range(rounds):
        symbols,oneVal = oneRound(k+1)
        res += oneVal
    return ' '.join(symbols)

def daySixteen2():
    pass

def daySixteen3():
    pass

def main():
    print("Hallo")
    print(daySixteen(), "ist die Lösung von Teil 1")
    #print(daySixteen2(), "ist die Lösung von Teil 2")
    #print(daySixteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()