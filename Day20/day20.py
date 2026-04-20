from typing import *
from collections import deque

def dayTwenty():
    # i,j,direction
    # direction: 0=NORTH, 1=EAST, 2=SOUTH, 3=WEST
    moves = {
        0: [(0, -1, 3), (-1, 0, 0), (0, 1, 1)],
        1: [(-1, 0, 0), (0, 1, 1), (1, 0, 2)],
        2: [(0, 1, 1), (1, 0, 2), (0, -1, 3)],
        3: [(1, 0, 2), (0, -1, 3), (-1, 0, 0)]
    }
    
    altitude = {"+":1, ".":-1, "-":-2}
    
    arr = []
    with open("Day20/20_1.txt") as file:
        for line in file:
            arr.append(line.strip())
    
    n,m = len(arr),len(arr[0])
    for j in range(m):
        if arr[0][j] == 'S':
            si,sj = 0,j
            break

    s = { (si,sj,d):1000 for d in range(4) }
    
    for _ in range(100):
        sn = {}
        for (i,j,d),alt in s.items():
            for di,dj,new_dir in moves[d]:
                ni,nj = i+di,j+dj
                if 0<=ni<n and 0<=nj<m and arr[ni][nj] in ".-+":
                    new_alt = alt + altitude[arr[ni][nj]]
                    key = (ni,nj,new_dir)
                    if key in sn:
                        sn[key] = max( sn[key],new_alt )
                    else:
                        sn[key] = new_alt
        s = sn
    
    return max(s.values())

def dayTwenty2():
    # i,j,direction
    # direction: 0=NORTH, 1=EAST, 2=SOUTH, 3=WEST
    moves = {
        0: [(0, -1, 3), (-1, 0, 0), (0, 1, 1)],
        1: [(-1, 0, 0), (0, 1, 1), (1, 0, 2)],
        2: [(0, 1, 1), (1, 0, 2), (0, -1, 3)],
        3: [(1, 0, 2), (0, -1, 3), (-1, 0, 0)]
    }
    
    altitude = {"+":1, ".":-1, "-":-2, "S":-1, "A":-1, "B":-1, "C":-1}
    checkpoints = "ABC"
    
    arr = []
    with open("Day20/20_2.txt") as file:
        for line in file:
            arr.append(line.strip())
    
    n,m = len(arr),len(arr[0])
    
    for j in range(m):
        if arr[0][j] == 'S':
            si,sj = 0,j
            break
    
    # (i,j,direction,checkpoint_index):altitude
    s = { (si,sj,d,0):10000 for d in range(4) }
    t = 0
    res = -1
    
    while res == -1:
        t += 1
        sn = {}
        for (i,j,d,p),alt in s.items():
            for di,dj,new_dir in moves[d]:
                ni,nj = i+di,j+dj
                if 0<=ni<n and 0<=nj<m and arr[ni][nj] in ".-+ABCS":
                    new_alt = alt + altitude[arr[ni][nj]]
                    
                    if arr[ni][nj] == 'S':
                        if new_alt >= 10000 and p == len(checkpoints):
                            res = t
                            break
                        continue
                    
                    new_p = p
                    if arr[ni][nj] in checkpoints:
                        if p == checkpoints.index(arr[ni][nj]):
                            new_p = p+1
                        else:
                            continue
                    
                    key = (ni,nj,new_dir,new_p)
                    sn[key] = max( sn.get(key,-float('inf')),new_alt )
        s = sn
    
    return res

def dayTwenty3():
    with open("Day20/20_3.txt") as file:
        lines = file.read().strip().split("\n")

    arr,start = [],(0,0)
    for y,line in enumerate(lines):
        row = []
        for x,c in enumerate(line):
            if c == "#": row.append(0)
            elif c == ".": row.append(3)
            elif c == "S": row.append(3); start = (x, y)
            elif c == "-": row.append(1)
            else: row.append(2)
        arr.append(row)

    h = len(arr)
    for _ in range(2):
        for r in range(h):
            arr.append(list(arr[r]))

    altitude_change = {0:0, 1:-2, 2:1, 3:-1}
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    m,n = len(arr),len(arr[0])

    def bfs(start_x,start_alt,alt_loss):
        q = deque()
        # (x,y,direction,altitude)
        q.append( (start_x,0,2,start_alt) )
        
        best = {}
        max_dist = 0

        while q:
            x,y,d,alt = q.popleft()

            if alt <= 0:
                if not alt_loss[start_x][3] and y > alt_loss[start_x][2]:
                    max_dist = max(max_dist,y)
                    alt_loss[start_x] = (alt_loss[start_x][0],x,y,False)
                continue

            key = (x,y,d)
            if key in best and best[key] >= alt:
                continue
            best[key] = alt

            if y == m-1:
                loss = start_alt-alt+1
                if loss < alt_loss[start_x][0]:
                    alt_loss[start_x] = (loss,x,y,True)
                continue

            for nd in [d, (d-1)%4, (d+1)%4]:
                nx,ny = x+dirs[nd][0], y+dirs[nd][1]
                if 0<=nx<n and 0<=ny<m and arr[ny][nx] != 0:
                    nalt = alt+altitude_change[arr[ny][nx]]
                    q.append( (nx,ny,nd,nalt) )

        return max_dist

    start_queue = [ (start[0],m+1) ]
    visited = set()
    alt_loss = {x:(10000,0,0,False) for x in range(n) if arr[0][x] != 0}

    while start_queue:
        x,alt = start_queue.pop()
        if x in visited:
            continue
        visited.add(x)
        bfs(x,alt,alt_loss)
        loss,fx,_,ok = alt_loss[x]
        if ok:
            start_queue.append( (fx,alt) )

    curr_x,curr_alt,segments = start[0],384400,0
    while curr_alt > 0:
        loss,fx,_,ok = alt_loss[curr_x]
        if not ok or curr_alt <= loss:
            break
        curr_alt -= loss
        curr_x = fx
        segments += 1

    final_loss = {x:(10000,0,0,False) for x in range(n) if arr[0][x] != 0}
    return segments*m + bfs(curr_x,curr_alt,final_loss)

def main():
    print("Hallo")
    print(dayTwenty(), "ist die Lösung von Teil 1")
    print(dayTwenty2(), "ist die Lösung von Teil 2")
    print(dayTwenty3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()