from collections import defaultdict, deque
from typing import *

def dayFive():
    tempArr = []
    #read
    with open("Day5/5_1.txt") as file:
        for line in file:
            tempArr.append([int(x) for x in line.strip().split()])
    arr = []
    for line in zip(*tempArr):
        arr.append(deque(list(line)))
    
    def calc_Round(curr_I):
        person = arr[curr_I].popleft()
        curr_I += 1
        if curr_I >= len(arr):
            curr_I = 0

        row_len = len( arr[curr_I] )
        left = person%row_len
        curr_mod = person//row_len
        if left == 0:
            left = row_len
            curr_mod -= 1

        if curr_mod%2 == 0:
            arr[curr_I].insert( left-1,person )
        else:
            arr[curr_I].insert( row_len-left+1,person )
        
        return int("".join([ str(x[0]) for x in arr]))

    curr_I = 0
    for _ in range(10):
        res = calc_Round(curr_I)
        curr_I += 1
        if curr_I >= len(arr):
            curr_I = 0
    return res

def dayFive2():
    tempArr = []
    #read
    with open("Day5/5_2.txt") as file:
        for line in file:
            tempArr.append([int(x) for x in line.strip().split()])
    arr = []
    for line in zip(*tempArr):
        arr.append(deque(list(line)))
    
    def calc_Round(curr_I):
        person = arr[curr_I].popleft()
        curr_I += 1
        if curr_I >= len(arr):
            curr_I = 0

        row_len = len( arr[curr_I] )
        left = person%row_len
        curr_mod = person//row_len
        if left == 0:
            left = row_len
            curr_mod -= 1

        if curr_mod%2 == 0:
            arr[curr_I].insert( left-1,person )
        else:
            arr[curr_I].insert( row_len-left+1,person )
        
        return int("".join([ str(x[0]) for x in arr]))

    seen = defaultdict(int)
    loop = 1
    curr_I = 0
    while True:
        res = calc_Round(curr_I)
        seen[(res)] += 1
        
        if seen[(res)] == 2024:
            return loop*res

        curr_I += 1
        if curr_I >= len(arr):
            curr_I = 0
        loop += 1

def dayFive3():
    tempArr = []
    #read
    with open("Day5/5_3.txt") as file:
        for line in file:
            tempArr.append([int(x) for x in line.strip().split()])
    arr = []
    for line in zip(*tempArr):
        arr.append(deque(list(line)))
    
    def calc_Round(curr_I):
        person = arr[curr_I].popleft()
        curr_I += 1
        if curr_I >= len(arr):
            curr_I = 0

        row_len = len( arr[curr_I] )
        left = person%row_len
        curr_mod = person//row_len
        if left == 0:
            left = row_len
            curr_mod -= 1

        if curr_mod%2 == 0:
            arr[curr_I].insert( left-1,person )
        else:
            arr[curr_I].insert( row_len-left+1,person )
        
        return int("".join([ str(x[0]) for x in arr]))

    seen = set()
    loop = 1
    max_shout = 0
    curr_I = 0
    while True:
        res = calc_Round(curr_I)

        curr_State = "".join("".join(str(x) for x in row) for row in arr)
        if curr_State in seen:
            return max_shout
        
        seen.add(curr_State)
        max_shout = max(max_shout,res)

        curr_I += 1
        if curr_I >= len(arr):
            curr_I = 0
        loop += 1

def main():
    print("Hallo")
    print(dayFive(), "ist die Lösung von Teil 1")
    print(dayFive2(), "ist die Lösung von Teil 2")
    print(dayFive3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()