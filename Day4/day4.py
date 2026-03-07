from typing import *

def dayFour():
    nails = []
    minNail = float("inf")
    #read
    with open("Day4/4_1.txt") as file:
        for line in file:
            nail = int(line.strip())
            nails.append(nail)
            minNail = min(minNail,nail)
    
    res = 0
    for nail in nails:
        res += nail-minNail
    return res

def dayFour2():
    nails = []
    minNail = float("inf")
    #read
    with open("Day4/4_2.txt") as file:
        for line in file:
            nail = int(line.strip())
            nails.append(nail)
            minNail = min(minNail,nail)
    
    res = 0
    for nail in nails:
        res += nail-minNail
    return res

def dayFour3():
    nails = []
    total = 0
    #read
    with open("Day4/4_3.txt") as file:
        for line in file:
            nail = int(line.strip())
            nails.append(nail)
            total += nail
    nails.sort()
    median = nails[len(nails)//2]
    
    res = 0
    for nail in nails:
            if nail >= median:
                res += nail-median
            else:
                res += median-nail
    return res

def main():
    print("Hallo")
    print(dayFour(), "ist die Lösung von Teil 1")
    print(dayFour2(), "ist die Lösung von Teil 2")
    print(dayFour3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()