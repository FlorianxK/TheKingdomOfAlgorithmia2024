from typing import *

def dayNineteen():
    dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    letter = {'R':1, 'L':-1}

    with open("Day19/19_1.txt") as file:
        rotate,arr = file.read().split("\n\n")
        arr = [list(line) for line in arr.split('\n')]
    m,n = len(arr),len(arr[0])
    y = 0
    for i in range(1,m-1):
        for j in range(1,n-1):
            l = rotate[y % len(rotate)]
            vals = [arr[i+di][j+dj] for (di,dj) in dirs]
            for x,val in enumerate(vals):
                di,dj = dirs[(x+letter[l]) % 8]
                arr[i+di][j+dj] = val
            y += 1

    return "".join(arr[1])[1:-1]
                
def dayNineteen2():
    dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    letter = {'R':1, 'L':-1}

    with open("Day19/19_2.txt") as file:
        rotate,arr = file.read().split("\n\n")
        arr = [list(line) for line in arr.split('\n')]
    m,n = len(arr),len(arr[0])

    def find_cycle():
        tempArr = [[(i,j) for j in range(n)] for i in range(m)]
        y = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                l = rotate[y % len(rotate)]
                vals = [tempArr[i+di][j+dj] for (di,dj) in dirs]
                for x,val in enumerate(vals):
                    di,dj = dirs[(x+letter[l]) % 8]
                    tempArr[i+di][j+dj] = val
                y += 1          

        transition = {}
        for i in range(m):
            for j in range(n):
                transition[tempArr[i][j]] = (i,j)

        cycles = []
        seen = set()
        for si in range(m):
            for sj in range(n):
                if (si,sj) in seen:
                    continue
                cycle = []
                i,j = si,sj
                while (i,j) not in seen:
                    cycle.append( (i,j) )
                    seen.add( (i,j) )
                    i,j = transition[i,j]
                cycles.append(cycle)
        return cycles

    def solve(rounds):
        cycles = find_cycle()
        newArr = [[None]*n for _ in range(m)]
        for cycle in cycles:
            for i,(si,sj) in enumerate(cycle):
                di,dj = cycle[(i+rounds) % len(cycle)]
                newArr[di][dj] = arr[si][sj]
        
        return "\n".join("".join(line) for line in newArr)

    finishedArr = solve(100)
    return finishedArr[finishedArr.index('>')+1:finishedArr.index('<')]

def dayNineteen3():
    dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    letter = {'R':1, 'L':-1}

    with open("Day19/19_3.txt") as file:
        rotate,arr = file.read().split("\n\n")
        arr = [list(line) for line in arr.split('\n')]
    m,n = len(arr),len(arr[0])

    def find_cycle():
        tempArr = [[(i,j) for j in range(n)] for i in range(m)]
        y = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                l = rotate[y % len(rotate)]
                vals = [tempArr[i+di][j+dj] for (di,dj) in dirs]
                for x,val in enumerate(vals):
                    di,dj = dirs[(x+letter[l]) % 8]
                    tempArr[i+di][j+dj] = val
                y += 1          

        transition = {}
        for i in range(m):
            for j in range(n):
                transition[tempArr[i][j]] = (i,j)

        cycles = []
        seen = set()
        for si in range(m):
            for sj in range(n):
                if (si,sj) in seen:
                    continue
                cycle = []
                i,j = si,sj
                while (i,j) not in seen:
                    cycle.append( (i,j) )
                    seen.add( (i,j) )
                    i,j = transition[i,j]
                cycles.append(cycle)
        return cycles

    def solve(rounds):
        cycles = find_cycle()
        newArr = [[None]*n for _ in range(m)]
        for cycle in cycles:
            for i,(si,sj) in enumerate(cycle):
                di,dj = cycle[(i+rounds) % len(cycle)]
                newArr[di][dj] = arr[si][sj]
        
        return "\n".join("".join(line) for line in newArr)

    finishedArr = solve(1048576000)
    return finishedArr[finishedArr.index('>')+1:finishedArr.index('<')]

def main():
    print("Hallo")
    print(dayNineteen(), "ist die Lösung von Teil 1")
    print(dayNineteen2(), "ist die Lösung von Teil 2")
    print(dayNineteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()