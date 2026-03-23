from collections import defaultdict, deque
from typing import *

def dayFifteen():
    arr = []
    herbs = set()
    i = 0
    #read
    with open("Day15/15_1.txt") as file:
        for line in file:
            line = line.strip()
            if i == 0:
                for j in range(len(line)):
                    if line[j] == '.':
                        start = (i,j)
            for j in range(len(line)):
                if line[j] == 'H':
                    herbs.add( (i,j) )
            i += 1
            arr.append( list(line) )
    m,n = len(arr),len(arr[0])

    seen = set()
    seen.add(start)
    # steps,pos
    q = deque([ (0,start) ])
    while q:
        steps,pos = q.popleft()
        if pos in herbs:
            return steps*2
        
        i,j = pos
        for di,dj in [ (-1,0),(1,0),(0,-1),(0,1) ]:
            ni,nj = i+di,j+dj
            if 0<=ni<m and 0<=nj<n and arr[ni][nj] != '#' and (ni,nj) not in seen:
                seen.add( (ni,nj) )
                q.append( (steps+1,(ni,nj)) )

def dayFifteen2():
    arr = []
    herbs = defaultdict(set)
    i = 0
    #read
    with open("Day15/15.txt") as file:
        for line in file:
            line = line.strip()
            if i == 0:
                for j in range(len(line)):
                    if line[j] == '.':
                        start = (i,j)
            for j in range(len(line)):
                if line[j] not in '.#~':
                    herbs[line[j]].add( (i,j) )
            i += 1
            arr.append( list(line) )
    m,n = len(arr),len(arr[0])

    print(dict(herbs))

    # steps,pos
    res = 0
    q = deque([ (0,start) ])
    while q:
        steps,pos = q.popleft()
        i,j = pos
        #check if on herb
        if arr[i][j] in herbs:
            l = arr[i][j]
            res += steps-1
            print(steps-1)
            q = deque([])
            # remove all double herbs
            for a,b in herbs[l]:
                arr[a][b] = '.'
            del herbs[l]
        #found all now go back
        if not herbs:
            # ERROR: must walk to A with 12 steps instead to B in 9 because collecting other herbs is faster. all permutations? try nearest A then nearest B then nearest C?
            return res
        
        for di,dj in [ (-1,0),(1,0),(0,-1),(0,1) ]:
            ni,nj = i+di,j+dj
            if 0<=ni<m and 0<=nj<n and arr[ni][nj] not in "#~":
                q.append( (steps+1,(ni,nj)) )

def dayFifteen3():
    pass

def main():
    print("Hallo")
    #print(dayFifteen(), "ist die Lösung von Teil 1")
    print(dayFifteen2(), "ist die Lösung von Teil 2")
    print(dayFifteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()