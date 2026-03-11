from collections import defaultdict, deque
from typing import *

def daySix():
    tree = defaultdict(list)
    paths = defaultdict(list)
    #read
    with open("Day6/6_1.txt") as file:
        for line in file:
            l,r = line.strip().split(':')
            tree[l] = r.split(',')

    # key,path,length
    q = deque([("RR","RR",1)])
    while q:
        curr,path,length = q.popleft()
        for ngh in tree[curr]:

            if ngh == '@':
                paths[length+1].append( path+ngh )
            else:
                q.append( (ngh,path+ngh,length+1) )
    for v in paths.values():
        if len(v) == 1:
            return v[0]
    
def daySix2():
    tree = defaultdict(list)
    paths = defaultdict(list)
    #read
    with open("Day6/6_2.txt") as file:
        for line in file:
            l,r = line.strip().split(':')
            tree[l] = r.split(',')

    # key,path,length
    q = deque([("RR","R",1)])
    while q:
        curr,path,length = q.popleft()
        for ngh in tree[curr]:

            if ngh == '@':
                paths[length+1].append( path+ngh )
            else:
                q.append( (ngh,path+ngh[0],length+1) )
    for v in paths.values():
        if len(v) == 1:
            return v[0]

def daySix3():
    tree = defaultdict(list)
    paths = defaultdict(list)
    #read
    with open("Day6/6_3.txt") as file:
        for line in file:
            l,r = line.strip().split(':')
            tree[l] = r.split(',')

    # key,path,length
    q = deque([("RR","R",1)])
    while True:
        nextQ = deque([])
        fruits = 0
        while q:
            curr,path,length = q.popleft()
            for ngh in tree[curr]:

                if ngh == '@':
                    paths[length+1].append( path+ngh )
                    fruits += 1
                else:
                    if ngh in {"BUG","ANT"}:
                        continue
                    nextQ.append( (ngh,path+ngh[0],length+1) )
        if fruits == 1:
            break
        else:
            q = nextQ

    for v in paths.values():
        if len(v) == 1:
            return v[0]

def main():
    print("Hallo")
    print(daySix(), "ist die Lösung von Teil 1")
    print(daySix2(), "ist die Lösung von Teil 2")
    print(daySix3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()