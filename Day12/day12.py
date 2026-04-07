from typing import *

def dayTwelve():
    arr = []
    #read
    with open("Day12/12_1.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
    
    def get_points():
        targets = []
        sources = []
        max_y = len(arr)-2
        for y,l in enumerate(arr):
            for x,c in enumerate(l):
                if c == 'T':
                    targets.append( (x,max_y-y) )
                elif c in "ABC":
                    sources.append( (x,max_y-y) )
        return targets,sources

    def get_power(source,target):
        dx = target[0]-source[0]
        dy = target[1]-source[1]
        if dx == dy:
            return int(dx)*(1+source[1])
        
        if dx-dy <= dy:
            return int(dy)*(1+source[1])
        
        if (dx+dy)%3 == 0:
            return (dx+dy)//3*(1+source[1])
        
        return float("inf")

    targets,sources = get_points()

    res = 0
    for t in targets:
        minVal = float("inf")
        for s in sources:
            minVal = min( minVal,get_power(s,t) )
        res += minVal
    return int(res)

def dayTwelve2():
    arr = []
    #read
    with open("Day12/12_2.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
    
    def get_points():
        targets = []
        sources = []
        hard = []
        max_y = len(arr)-2
        for y,l in enumerate(arr):
            for x,c in enumerate(l):
                if c in "TH":
                    targets.append( (x,max_y-y) )
                    hard.append( 2 if c == 'H' else 1 )
                elif c in "ABC":
                    sources.append( (x,max_y-y) )
        return targets,sources,hard

    def get_power(source,target):
        dx = target[0]-source[0]
        dy = target[1]-source[1]
        if dx == dy:
            return int(dx)*(1+source[1])
        
        if dx-dy <= dy:
            return int(dy)*(1+source[1])
        
        if (dx+dy)%3 == 0:
            return (dx+dy)//3*(1+source[1])
        
        return float("inf")

    targets,sources,hard = get_points()

    res = 0
    for t,h in zip(targets,hard):
        minVal = float("inf")
        for s in sources:
            minVal = min( minVal,get_power(s,t) )
        res += h*minVal
    return int(res)

def dayTwelve3():
    pass

def main():
    print("Hallo")
    print(dayTwelve(), "ist die Lösung von Teil 1")
    print(dayTwelve2(), "ist die Lösung von Teil 2")
    print(dayTwelve3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()