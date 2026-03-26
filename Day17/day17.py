from collections import defaultdict
import heapq
from typing import *

def daySeventeen():
    arr = []
    with open("Day17/17_1.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
    
    stars = []
    m, n = len(arr),len(arr[0])
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '*':
                stars.append((j+1,m-i))

    edges = []
    for i in range(len(stars)):
        for j in range(i+1,len(stars)):
            a,b = stars[i],stars[j]
            dist = abs(a[0]-b[0]) + abs(a[1]-b[1])
            heapq.heappush(edges, (dist,i,j))
    
    parent = list(range(len(stars)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a,b):
        rootA = find(a)
        rootB = find(b)
        if rootA == rootB:
            return False
        parent[rootB] = rootA
        return True

    res = 0
    edges_used = 0

    while edges and edges_used < len(stars)-1:
        dist,i,j = heapq.heappop(edges)
        if union(i,j):
            res += dist
            edges_used += 1

    return len(stars)+res

def daySeventeen2():
    arr = []
    with open("Day17/17_2.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
    
    stars = []
    m, n = len(arr),len(arr[0])
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '*':
                stars.append((j+1,m-i))

    edges = []
    for i in range(len(stars)):
        for j in range(i+1,len(stars)):
            a,b = stars[i],stars[j]
            dist = abs(a[0]-b[0]) + abs(a[1]-b[1])
            heapq.heappush(edges, (dist,i,j))
    
    parent = list(range(len(stars)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a,b):
        rootA = find(a)
        rootB = find(b)
        if rootA == rootB:
            return False
        parent[rootB] = rootA
        return True

    res = 0
    edges_used = 0

    while edges and edges_used < len(stars)-1:
        dist,i,j = heapq.heappop(edges)
        if union(i,j):
            res += dist
            edges_used += 1

    return len(stars)+res

def daySeventeen3():
    arr = []
    with open("Day17/17_3.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
    
    stars = []
    m,n = len(arr),len(arr[0])
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '*':
                stars.append((j+1,m-i))
    
    adj = defaultdict(list)
    for i in range(len(stars)):
        for j in range(i+1,len(stars)):
            a,b = stars[i],stars[j]
            dist = abs(a[0]-b[0]) + abs(a[1]-b[1])
            if dist < 6:
                adj[a].append((dist,b))
                adj[b].append((dist,a))

    stars = set(stars)
    sizes = []
    while stars:
        h = [ (0,stars.pop()) ]
        total_dist = 0
        seen = set()
        while h:
            dist,star = heapq.heappop(h)
            if star in seen:
                continue
            total_dist += dist
            seen.add(star)
            for nextDist, nextStar in adj[star]:
                if nextStar not in seen:
                    heapq.heappush(h, (nextDist,nextStar) )
        sizes.append(total_dist+len(seen))
        stars = stars-seen

    sizes.sort()
    return sizes[-1]*sizes[-2]*sizes[-3]

def main():
    print("Hallo")
    print(daySeventeen(), "ist die Lösung von Teil 1")
    print(daySeventeen2(), "ist die Lösung von Teil 2")
    print(daySeventeen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()