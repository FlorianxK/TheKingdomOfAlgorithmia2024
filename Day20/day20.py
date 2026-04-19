from typing import *

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
    pass

def main():
    print("Hallo")
    print(dayTwenty(), "ist die Lösung von Teil 1")
    print(dayTwenty2(), "ist die Lösung von Teil 2")
    #print(dayTwenty3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()