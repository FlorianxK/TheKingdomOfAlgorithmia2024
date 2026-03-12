from collections import deque
import heapq
from typing import *

def daySeven():

    def race(arr,segments):
        res = 0
        power = 10
        index = 0
        for _ in range(segments):
            if arr[index] == '+':
                power += 1
            elif arr[index] == '-' and power > 0:
                power -= 1
            
            res += power
            index = (index+1)%len(arr)

        return res

    res = []
    #read
    with open("Day7/7_1.txt") as file:
        for line in file:
            l,r = line.strip().split(':')
            arr = r.split(',')
            essence = race(arr,10)
            heapq.heappush(res, (-essence,l) )
    
    order = ""
    while res:
        _,letter = heapq.heappop(res)
        order += letter
    return order
    
def daySeven2():

    def race(arr,track,rounds):
        n = len(track)
        res = 0
        power = 10
        index = 0

        for _ in range(rounds):
            for k in range(n):
                if track[k] == '+':
                    power += 1
                elif track[k] == '-' and power > 0:
                    power -= 1
                elif track[k] in "S=":

                    if arr[index] == '+':
                        power += 1
                    elif arr[index] == '-' and power > 0:
                        power -= 1
                
                res += power
                index = (index+1)%len(arr)

        return res

    res = []
    #read
    with open("Day7/track1.txt") as file:
        track = [list(x) for x in file.read().split('\n')]
    m,n = len(track),len(track[0])
    track_loop = []
    for j in range(1,n):
        track_loop.append( track[0][j] )
    for i in range(1,m):
        track_loop.append( track[i][n-1] )
    for j in range(n-2,-1,-1):
        track_loop.append( track[m-1][j] )
    for i in range(m-2,-1,-1):
        track_loop.append( track[i][0] )

    rounds = 10
    with open("Day7/7_2.txt") as file:
        for line in file:
            l,r = line.strip().split(':')
            arr = r.split(',')
            essence = race(arr,track_loop,rounds)
            heapq.heappush(res, (-essence,l) )
    
    order = ""
    while res:
        _,letter = heapq.heappop(res)
        order += letter
    return order

def daySeven3():
    def race(arr,track,rounds):
        n = len(track)
        res = 0
        power = 10
        index = 0

        for _ in range(rounds):
            for k in range(n):
                if track[k] == '+':
                    power += 1
                elif track[k] == '-' and power > 0:
                    power -= 1
                elif track[k] in "S=":

                    if arr[index] == '+':
                        power += 1
                    elif arr[index] == '-' and power > 0:
                        power -= 1
                
                res += power
                index = (index+1)%len(arr)

        return res

    #read
    with open("Day7/track2.txt") as file:
        track = [list(x) for x in file.read().split('\n')]
    m,n = len(track),len(track[0])

    for i in range(m):
        if len(track[i]) < n:
            track[i].extend( ' '*(n-len(track[i])) )

    track_loop = []
    d = deque([(0,1)])
    seen = set()
    seen.add((0,1))
    while d:
        curr = d.popleft()
        i,j = curr
        track_loop.append(track[i][j])
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj = i+di,j+dj
            if 0<=ni<m and 0<=nj<n and (ni,nj) not in seen:
                if track[ni][nj] == ' ':
                    continue
                if track[ni][nj] == 'S':
                    if len(track_loop) > 1:
                        track_loop.append('S')
                else:
                    seen.add((ni,nj))
                    d.append( (ni,nj) )

    rounds = 11
    with open("Day7/7_3.txt") as file:
        for line in file:
            l,r = line.strip().split(':')
            arr = r.split(',')
            essence = race(arr,track_loop,rounds)

    def generate(expr="",plus=5,minus=3,equal=3):
        if plus == 0 and minus == 0 and equal == 0:
            yield expr
            return
        if plus > 0:
            yield from generate(expr+"+",plus-1,minus,equal)
        if minus > 0:
            yield from generate(expr+"-",plus,minus-1,equal)
        if equal > 0:
            yield from generate(expr+"=",plus,minus,equal-1)

    plans = 0
    tactics = list(generate())
    c = 1
    for t in tactics:
        res = race(t,track_loop,rounds)
        #print(f"{c}: {res}")
        c += 1
        if res > essence:
            plans += 1
    return plans

def main():
    print("Hallo")
    print(daySeven(), "ist die Lösung von Teil 1")
    print(daySeven2(), "ist die Lösung von Teil 2")
    print(daySeven3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()