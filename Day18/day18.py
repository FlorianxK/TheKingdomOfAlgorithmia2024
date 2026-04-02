from collections import deque
from typing import *

def dayEighteen():
    arr = []
    palms = set()
    i = 0
    with open("Day18/18_1.txt") as file:
        for line in file:
            arr.append( list(line.strip()) )
            for j in range(len(line)):
                if line[j] == 'P':
                    palms.add( (i,j) )
            i += 1

    m,n = len(arr),len(arr[0])
    #find start
    for j in range(n):
        if arr[0][j] == '.':
            start = (0,j)
        elif arr[m-1][j] == '.':
            start = (m-1,j)
    for i in range(m):
        if arr[i][0] == '.':
            start = (i,0)
        elif arr[i][n-1] == '.':
            start = (i,n-1)

    # time,pos
    q = deque([(0,start)])
    seen = set()
    seen.add(start)

    while q:
        time,pos = q.popleft()
        i,j = pos
        
        if pos in palms:
            palms.remove(pos)
            if not palms:
                return time
        
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj = i+di,j+dj
            if 0<=ni<m and 0 <=nj<n and arr[ni][nj] != '#' and (ni,nj) not in seen:
                seen.add( (ni,nj) )
                q.append( (time+1,(ni,nj)) )
                
def dayEighteen2():
    arr = []
    palms = set()
    i = 0
    with open("Day18/18_2.txt") as file:
        for line in file:
            arr.append( list(line.strip()) )
            for j in range(len(line)):
                if line[j] == 'P':
                    palms.add( (i,j) )
            i += 1

    m,n = len(arr),len(arr[0])
    starts = []
    #find starts
    for j in range(n):
        if arr[0][j] == '.':
            starts.append( (0,j) )
        elif arr[m-1][j] == '.':
            starts.append( (m-1,j) )
    for i in range(m):
        if arr[i][0] == '.':
            starts.append( (i,0) )
        elif arr[i][n-1] == '.':
            starts.append( (i,n-1) )

    # time,pos
    q = deque([])
    seen = set()
    for start in starts:
        q.append( (0,start) )
        seen.add(start)

    while True:
        nextQ = deque([])
        while q:
            time,pos = q.popleft()
            i,j = pos
            
            if pos in palms:
                palms.remove(pos)
                if not palms:
                    return time
            
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = i+di,j+dj
                if 0<=ni<m and 0 <=nj<n and arr[ni][nj] != '#' and (ni,nj) not in seen:
                    seen.add( (ni,nj) )
                    nextQ.append( (time+1,(ni,nj)) )
        
        if nextQ:
            q = nextQ
        else:
            break

def dayEighteen3():
    arr = []
    palms = set()
    i = 0
    with open("Day18/18_3.txt") as file:
        for line in file:
            arr.append( list(line.strip()) )
            for j in range(len(line)):
                if line[j] == 'P':
                    palms.add( (i,j) )
            i += 1

    m,n = len(arr),len(arr[0])

    def bfs_distances(start:tuple):
        level = [start]
        time = 0
        seen = Counter()
        while level:
            nextLevel = []
            for pos in level:
                if pos in seen:
                    continue
                seen[pos] = time
                i,j = pos
                for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni,nj = i+di,j+dj
                    if 0<=ni<m and 0 <=nj<n and arr[ni][nj] != '#' and (ni,nj) not in seen:
                        nextLevel.append( (ni,nj) )
            time += 1
            level = nextLevel
        return seen

    total_distances = Counter()
    for sp in palms:
        total_distances += bfs_distances(sp)
    
    return min(total_distances[c] for c in total_distances if c not in palms)

def main():
    print("Hallo")
    print(dayEighteen(), "ist die Lösung von Teil 1")
    print(dayEighteen2(), "ist die Lösung von Teil 2")
    print(dayEighteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()