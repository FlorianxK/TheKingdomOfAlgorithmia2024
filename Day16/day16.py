from collections import defaultdict
from functools import cache
from itertools import zip_longest
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
    for k in range(1,rounds+1):
        symbols,oneVal = oneRound(k)
        res += oneVal
    return ' '.join(symbols)

def daySixteen2():
    arr = []
    #read
    with open("Day16/16_2.txt") as file:
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
        c = Counter()
        for i in range(len(spin)):
            v = slotRows[i+1]
            indices[i] = (indices[i]+spin[i])%len(v)
            val = v[ indices[i] ]
            cat = Counter()
            cat[val[0]] += 1
            cat[val[-1]] += 1
            c = c+cat

        coins = 0
        for v in c.values():
            if v >= 3:
                coins += 1
                coins += v-3
        return coins
    
    res = 0
    rounds = 202420242024
    oneVal_list = []
    seen = {}
    for k in range(1,rounds+1):
        oneVal = oneRound(k)
        oneVal_list.append(oneVal)
        res += oneVal

        state = tuple(indices)
        if state in seen:
            first_seen = seen[state]
            cycle_length = k-first_seen
            cycle_values = oneVal_list[first_seen:k]
            cycle_sum = sum(cycle_values)
            remain = rounds-k
            res += (remain // cycle_length) * cycle_sum
            for i in range(remain % cycle_length):
                res += cycle_values[i]
            break
        seen[state] = k
    return res
    
def daySixteen3():
    with open("Day16/16_3.txt") as file:
        header,_,*remainder = file.read().splitlines()
    
    wheel_distances = [int(x) for x in header.split(",")]
    wheels_transpose = []
    for line in remainder:
        row_symbols = []
        for i in range(0,len(line),4):
            symbol = line[i:i+3].strip()
            row_symbols.append(symbol)
        wheels_transpose.append(row_symbols)
    
    wheels = []
    for wheel_symbols in zip_longest(*wheels_transpose, fillvalue=""):
        filtered = [s for s in wheel_symbols if s]
        processed = [w[::2] for w in filtered]
        wheels.append(tuple(processed))

    @cache
    def maxmin_score(wheel_offset=0,pull_number=0,pulls_remaining=256):
        symbols = []
        for dist,wheel in zip(wheel_distances,wheels):
            index = (pull_number * dist + wheel_offset) % len(wheel)
            symbol = wheel[index]
            symbols.append(symbol)
        line = "".join(symbols)
        if pull_number:
            counts = Counter(line)
            score = 0
            for count in counts.values():
                if count > 2:
                    score += count-2
        else:
            score = 0
        if pulls_remaining:
            results = []
            for i in (-1,0,1):
                result = maxmin_score(wheel_offset+i,pull_number+1,pulls_remaining-1)
                results.append(result)
            maxs = [r[0] for r in results]
            mins = [r[1] for r in results]
            return score+max(maxs), score+min(mins)
        return score,score

    maxRes,minRes = maxmin_score()
    return f"{maxRes} {minRes}"
    
def main():
    print("Hallo")
    print(daySixteen(), "ist die Lösung von Teil 1")
    print(daySixteen2(), "ist die Lösung von Teil 2")
    print(daySixteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()