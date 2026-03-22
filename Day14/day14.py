from collections import deque
from typing import *

def dayFourteen():
    maxHeight = 0
    #read
    with open("Day14/14_1.txt") as file:
        arr = file.read().strip().split(',')
        currHeight = 0
        for move in arr:
            direction = move[0]
            val = int( move[1:] )
            if direction == 'U':
                currHeight += val
                maxHeight = max(maxHeight,currHeight)
            elif direction == 'D':
                currHeight = max(0,currHeight-val)
    return maxHeight

def dayFourteen2():
    segments = set()
    #read
    with open("Day14/14_2.txt") as file:
        for line in file:
            arr = line.strip().split(',')
            # x,y,z
            currPos = (0,0,0)
            for move in arr:
                direction = move[0]
                val = int( move[1:] )
                x,y,z = currPos
                for _ in range(1,val+1):
                    if direction == 'U':
                        y += 1
                    elif direction == 'D':
                        y = max(0,y-1)
                    elif direction == 'R':
                        x += 1
                    elif direction == 'L':
                        x -= 1
                    elif direction == 'F':
                        z += 1
                    elif direction == 'B':
                        z -= 1
                    
                    currPos = (x,y,z)
                    if currPos not in segments:
                        segments.add( currPos )
        
        return len(segments)

def dayFourteen3():
    segments = set()
    leaves = set()
    #read
    with open("Day14/14_3.txt") as file:
        for line in file:
            arr = line.strip().split(',')
            # x,y,z
            currPos = (0,0,0)
            for move in arr:
                direction = move[0]
                val = int( move[1:] )
                x,y,z = currPos
                for _ in range(1,val+1):
                    if direction == 'U':
                        y += 1
                    elif direction == 'D':
                        y = max(0,y-1)
                    elif direction == 'R':
                        x += 1
                    elif direction == 'L':
                        x -= 1
                    elif direction == 'F':
                        z += 1
                    elif direction == 'B':
                        z -= 1
                    
                    currPos = (x,y,z)
                    if currPos not in segments:
                        segments.add( currPos )
            leaves.add(currPos)
        
        starts = []
        for x,y,z in segments:
            if x == 0 and z == 0:
                starts.append( (x,y,z) )

        distances = []
        for start in starts:
            # weg,pos
            q = deque([ (0,start) ])
            seen = set()
            seen.add(start)
            dist = 0
            while q:
                steps,(x,y,z) = q.popleft()

                if (x,y,z) in leaves:
                    dist += steps
                    continue

                for dx,dy,dz in [ (1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1) ]:
                    nx,ny,nz = x+dx,y+dy,z+dz
                    if (nx,ny,nz) in seen:
                        continue

                    if (nx,ny,nz) in segments:
                        q.append( (steps+1,(nx,ny,nz)) )
                        seen.add( (nx,ny,nz) )
            
            distances.append(dist)
        return min(distances)

def main():
    print("Hallo")
    print(dayFourteen(), "ist die Lösung von Teil 1")
    print(dayFourteen2(), "ist die Lösung von Teil 2")
    print(dayFourteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()