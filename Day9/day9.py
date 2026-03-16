from functools import cache
from typing import *

def dayNine():
    res = 0
    stamps = [1, 3, 5, 10]
    #read
    with open("Day9/9_1.txt") as file:
        for line in file:
            spark = int(line.strip())
            bettles = 0
            for i in range(len(stamps)-1,-1,-1):
                if stamps[i] <= spark:
                    temp = spark//stamps[i]
                    bettles += temp
                    spark -= temp*stamps[i]
            res += bettles
    return res

def dayNine2():

    @cache
    def find_min(brightness):
        if brightness == 0:
            return 0
        if brightness < 0:
            return float("inf")
        best = float("inf")
        for stamp in stamps:
            sub = find_min(brightness-stamp)
            best = min(best,1+sub)
        return best
    
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    stamps.reverse()
    res = 0
    #read
    with open("Day9/9_2.txt") as file:
        for line in file:
            spark = int(line.strip())
            res += find_min(spark)
    return res

def dayNine3():

    @cache
    def find_min(brightness):
        if brightness == 0:
            return 0
        if brightness < 0:
            return float("inf")
        best = float("inf")
        for stamp in stamps:
            sub = find_min(brightness-stamp)
            best = min(best,1+sub)
        return best
    
    def two_balls(brightness):
        hb1 = brightness//2
        hb2 = brightness-hb1
        minList = float("inf")
        for i in range( 51-brightness%2 ):
            temp = find_min(hb1-i)+find_min(hb2+i)
            minList = min(minList,temp)
        return minList
    
    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    stamps.reverse()
    res = 0
    #read
    with open("Day9/9_3.txt") as file:
        for line in file:
            spark = int(line.strip())
            res += two_balls(spark)
    return res

def main():
    print("Hallo")
    print(dayNine(), "ist die Lösung von Teil 1")
    print(dayNine2(), "ist die Lösung von Teil 2")
    print(dayNine3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()