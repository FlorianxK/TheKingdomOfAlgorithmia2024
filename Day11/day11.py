from collections import defaultdict
from typing import *

def dayTwelve():
    d = defaultdict(list)
    #read
    with open("Day11/11_1.txt") as file:
        for line in file:
            l,r = line.strip().split(':')
            d[l] = r.split(',')
    state = ['A']
    days = 4
    for _ in range(days):
        nextState = []
        for s in state:
            nextState.extend( d[s] )
        state = nextState
    return len(state)

def dayTwelve2():
    d = defaultdict(list)
    #read
    with open("Day11/11_2.txt") as file:
        for line in file:
            l,r = line.strip().split(':')
            d[l] = r.split(',')
    state = ['Z']
    days = 10
    for _ in range(days):
        nextState = []
        for s in state:
            nextState.extend( d[s] )
        state = nextState
    return len(state)

def dayTwelve3():
    d = defaultdict(list)
    #read
    with open("Day11/11_3.txt") as file:
        for line in file:
            l,r = line.strip().split(':')
            d[l] = Counter(r.split(','))
    minState = float("inf")
    maxState = -float("inf")
    days = 20
    for k in d.keys():
        state = Counter({k: 1})
        for _ in range(days):
            nextState = Counter()
            for a,aCount in state.items():
                for b,bCount in d[a].items():
                    nextState[b] += aCount*bCount
            state = nextState
        v = sum(state.values())
        minState = min(minState,v)
        maxState = max(maxState,v)

    return maxState-minState

def main():
    print("Hallo")
    print(dayTwelve(), "ist die Lösung von Teil 1")
    print(dayTwelve2(), "ist die Lösung von Teil 2")
    print(dayTwelve3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()