import heapq
from typing import *

def dayThirteen():
    arr = []
    i = 0
    #read
    with open("Day13/13_1.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
                elif line[j] == 'E':
                    end = (i,j)
            i += 1

    def height_diff(a,b):
        return min( abs(a-b),abs(a-b+10),abs(a-b-10) )

    m,n = len(arr),len(arr[0])
    arr[start[0]][start[1]] = '0'
    arr[end[0]][end[1]] = '0'
    # distance,position
    h = []
    heapq.heappush(h,(0,start))
    dists = [ [float("inf")]*n for _ in range(m) ]
    dists[start[0]][start[1]] = 0
    while h:
        d,pos = heapq.heappop(h)
        if pos == end:
            return d

        i,j = pos
        if d > dists[i][j]:
            continue

        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj = i+di,j+dj
            if 0<=ni<m and 0<=nj<n and arr[ni][nj] != '#':
                new_dist = d + height_diff(int(arr[i][j]),int(arr[ni][nj]))+1

                if new_dist < dists[ni][nj]:
                    dists[ni][nj] = new_dist
                    heapq.heappush(h, (new_dist,(ni,nj)) )

def dayThirteen2():
    arr = []
    i = 0
    #read
    with open("Day13/13_2.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
                elif line[j] == 'E':
                    end = (i,j)
            i += 1

    def height_diff(a,b):
        return min( abs(a-b),abs(a-b+10),abs(a-b-10) )

    m,n = len(arr),len(arr[0])
    arr[start[0]][start[1]] = '0'
    arr[end[0]][end[1]] = '0'
    # distance,position
    h = []
    heapq.heappush(h,(0,start))
    dists = [ [float("inf")]*n for _ in range(m) ]
    dists[start[0]][start[1]] = 0
    while h:
        d,pos = heapq.heappop(h)
        if pos == end:
            return d

        i,j = pos
        if d > dists[i][j]:
            continue

        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj = i+di,j+dj
            if 0<=ni<m and 0<=nj<n and arr[ni][nj] != '#':
                new_dist = d + height_diff(int(arr[i][j]),int(arr[ni][nj]))+1

                if new_dist < dists[ni][nj]:
                    dists[ni][nj] = new_dist
                    heapq.heappush(h, (new_dist,(ni,nj)) )

def dayThirteen3():
    arr = []
    starts = []
    i = 0
    #read
    with open("Day13/13_3.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
            for j in range(len(line)):
                if line[j] == 'S':
                    starts.append( (i,j) )
                elif line[j] == 'E':
                    end = (i,j)
            i += 1

    def height_diff(a,b):
        return min( abs(a-b),abs(a-b+10),abs(a-b-10) )

    m,n = len(arr),len(arr[0])
    for a,b in starts:
        arr[a][b] = '0'
    arr[end[0]][end[1]] = '0'
    time = float("inf")
    for start in starts:
        # distance,position
        h = []
        heapq.heappush(h,(0,start))
        dists = [ [float("inf")]*n for _ in range(m) ]
        dists[start[0]][start[1]] = 0
        while h:
            d,pos = heapq.heappop(h)
            if pos == end:
                time = min(time,d)
                break

            i,j = pos
            if d > dists[i][j]:
                continue

            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = i+di,j+dj
                if 0<ni<m-1 and 0<nj<n-1 and arr[ni][nj] != '#':
                    new_dist = d + height_diff(int(arr[i][j]),int(arr[ni][nj]))+1

                    if new_dist < dists[ni][nj]:
                        dists[ni][nj] = new_dist
                        heapq.heappush(h, (new_dist,(ni,nj)) )
    return time

def main():
    print("Hallo")
    print(dayThirteen(), "ist die Lösung von Teil 1")
    print(dayThirteen2(), "ist die Lösung von Teil 2")
    print(dayThirteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()