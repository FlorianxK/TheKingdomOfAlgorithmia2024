from typing import *

def dayOne():
    amount = 0
    #read
    with open("Day1/1_1.txt") as file:
        arr = [x for x in file.read()]
    
    for p in arr:
        if p == 'B':
            amount += 1
        elif p == 'C':
            amount += 3
    return amount
            
def dayOne2():
    amount = 0
    d = {'A':0, 'B':1, 'C':3, 'D':5}
    #read
    with open("Day1/1_2.txt") as file:
        arr = [x for x in file.read()]

    for i in range(1,len(arr),2):
        if arr[i-1] == 'x' and arr[i] == 'x':
            continue
        elif arr[i-1] == 'x':
            amount += d[arr[i]]
        elif arr[i] == 'x':
            amount += d[arr[i-1]]
        else:
            amount += d[arr[i-1]]+d[arr[i]]+2
    return amount

def dayOne3():
    amount = 0
    d = {'A':0, 'B':1, 'C':3, 'D':5}
    #read
    with open("Day1/1_3.txt") as file:
        arr = [x for x in file.read()]

    groups = [arr[i:i+3] for i in range(0,len(arr),3)]
    for g in groups:
        c = g.count('x')
        for member in g:
            if member == 'x':
                continue
            amount += d[member]+2-c
    return amount

def main():
    print("Hallo")
    print(dayOne(), "ist die Lösung von Teil 1")
    print(dayOne2(), "ist die Lösung von Teil 2")
    print(dayOne3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()