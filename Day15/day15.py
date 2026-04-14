from collections import defaultdict, deque
from functools import cache
from itertools import permutations
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
    arr = {}
    herbs = defaultdict(list)
    i = 0
    #read
    with open("Day15/15_2.txt") as file:
        for line in file:
            line = line.strip()
            if i == 0:
                for j in range(len(line)):
                    if line[j] == '.':
                        start = (i,j)
            for j in range(len(line)):
                if line[j] not in "#~":
                    arr[(i,j)] = line[j]
                if line[j] not in ".#~":
                    herbs[line[j]].append( (i,j) )
            i += 1

    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    needed = [start]
    for h in herbs.values():
        needed.extend(h)
    all_costs = {}
    for s in needed:
        all_costs[s] = costs = {pos:float("inf") for pos in arr}
        costs[s] = 0
        to_update = set()
        for di,dj in dirs:
            i,j = s
            ni,nj = di+i,dj+j
            if (ni,nj) in arr:
                to_update.add( (ni,nj) )

        while to_update:
            new_update = set()
            for loc in to_update:
                nghs = []
                nghs_costs = []
                for di,dj in dirs:
                    i,j = loc
                    ni,nj = di+i,dj+j
                    if (ni,nj) in arr:
                        nghs.append( (ni,nj) )
                        nghs_costs.append( costs[(ni,nj)] )
                new_cost = min(nghs_costs)+1
                if new_cost < costs[loc]:
                    costs[loc] = new_cost
                    new_update.update(nghs)
            to_update = new_update
    
    @cache
    def min_cost_order(current,remaining_herbs,end):
        if not remaining_herbs:
            return all_costs[current][end]
        next_herb = remaining_herbs[0]
        next_locations = herbs[next_herb]
        return min(all_costs[current][next_loc]+min_cost_order(next_loc,remaining_herbs[1:],end) for next_loc in next_locations)

    times = [min_cost_order(start,perm,start) for perm in permutations(herbs)]
    return min(times)

def dayFifteen3():
    arr = {}
    herbs = defaultdict(list)
    i = 0
    #read
    with open("Day15/15_3.txt") as file:
        for line in file:
            line = line.strip()
            if i == 0:
                for j in range(len(line)):
                    if line[j] == '.':
                        start = (i,j)
            for j in range(len(line)):
                if line[j] not in "#~":
                    arr[(i,j)] = line[j]
                if line[j] not in ".#~":
                    herbs[line[j]].append( (i,j) )
            i += 1
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    needed = [start]
    for h in herbs.values():
        needed.extend(h)
    all_costs = {}
    for s in needed:
        all_costs[s] = costs = {pos:float("inf") for pos in arr}
        costs[s] = 0
        to_update = set()
        for di,dj in dirs:
            i,j = s
            ni,nj = di+i,dj+j
            if (ni,nj) in arr:
                to_update.add( (ni,nj) )

        while to_update:
            new_update = set()
            for loc in to_update:
                nghs = []
                nghs_costs = []
                for di,dj in dirs:
                    i,j = loc
                    ni,nj = di+i,dj+j
                    if (ni,nj) in arr:
                        nghs.append( (ni,nj) )
                        nghs_costs.append( costs[(ni,nj)] )
                new_cost = min(nghs_costs)+1
                if new_cost < costs[loc]:
                    costs[loc] = new_cost
                    new_update.update(nghs)
            to_update = new_update
    
    @cache
    def min_cost_order(current,remaining_herbs,end):
        if not remaining_herbs:
            return all_costs[current][end]
        next_herb = remaining_herbs[0]
        next_locations = herbs[next_herb]
        return min(all_costs[current][next_loc]+min_cost_order(next_loc,remaining_herbs[1:],end) for next_loc in next_locations)

    mid_e = max(herbs["E"])
    mid_r = min(herbs["R"])
    abcde = min(min_cost_order(mid_e,perm,mid_e) for perm in permutations("ABCDE"))
    ghijk = min(min_cost_order(start,perm,start) for perm in permutations("EGHIJKR"))
    nopqr = min(min_cost_order(mid_r,perm,mid_r) for perm in permutations("NOPQR"))
    return abcde+ghijk+nopqr

def main():
    print("Hallo")
    print(dayFifteen(), "ist die Lösung von Teil 1")
    print(dayFifteen2(), "ist die Lösung von Teil 2")
    print(dayFifteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()