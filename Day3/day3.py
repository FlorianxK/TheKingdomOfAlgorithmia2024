from typing import *

def dayThree():
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    blocks = set()
    i = 0
    #read
    with open("Day3/3_1.txt") as file:
        for line in file:
            for j in range(len(line)):
                if line[j] == '#':
                    blocks.add( (i,j) )
            i += 1

    def dig():
        newBlocks = set()
        for i,j in blocks:
            ngh = 0
            for di,dj in dirs:
                ni,nj = i+di,j+dj
                if (ni,nj) in blocks:
                    ngh += 1
            if ngh == 4:
                newBlocks.add( (i,j) )
        return newBlocks

    res = len(blocks)
    while blocks:
        blocks = dig()
        res += len(blocks)
    return res

def dayThree2():
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    blocks = set()
    i = 0
    #read
    with open("Day3/3_2.txt") as file:
        for line in file:
            for j in range(len(line)):
                if line[j] == '#':
                    blocks.add( (i,j) )
            i += 1

    def dig():
        newBlocks = set()
        for i,j in blocks:
            ngh = 0
            for di,dj in dirs:
                ni,nj = i+di,j+dj
                if (ni,nj) in blocks:
                    ngh += 1
            if ngh == 4:
                newBlocks.add( (i,j) )
        return newBlocks

    res = len(blocks)
    while blocks:
        blocks = dig()
        res += len(blocks)
    return res

def dayThree3():
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
    blocks = set()
    i = 0
    #read
    with open("Day3/3_3.txt") as file:
        for line in file:
            for j in range(len(line)):
                if line[j] == '#':
                    blocks.add( (i,j) )
            i += 1

    def dig():
        newBlocks = set()
        for i,j in blocks:
            ngh = 0
            for di,dj in dirs:
                ni,nj = i+di,j+dj
                if (ni,nj) in blocks:
                    ngh += 1
            if ngh == 8:
                newBlocks.add( (i,j) )
        return newBlocks

    res = len(blocks)
    while blocks:
        blocks = dig()
        res += len(blocks)
    return res

def main():
    print("Hallo")
    print(dayThree(), "ist die Lösung von Teil 1")
    print(dayThree2(), "ist die Lösung von Teil 2")
    print(dayThree3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()