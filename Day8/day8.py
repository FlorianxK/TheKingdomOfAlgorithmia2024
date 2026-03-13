from collections import deque
import heapq
from typing import *

def dayEight():
    #read
    with open("Day8/8_1.txt") as file:
        available = int(file.read().strip())
    width = 1
    currAmount = 1
    while currAmount < available:
        width += 2
        currAmount += width
    
    return (currAmount-available)*width
    
def dayEight2():
    #read
    with open("Day8/8_2.txt") as file:
        nullpointers = int(file.read().strip())
    
    acolytes = 1111
    available = 20240000
    
    width = 1
    currAmount = 1
    lastThickness = 1
    while currAmount < available:
        newThickness = (lastThickness*nullpointers)%acolytes
        lastThickness = newThickness
        width += 2
        currAmount += width*newThickness
    return (currAmount-available)*width

def dayEight3():
    #read
    with open("Day8/8_3.txt") as file:
        nullpointers = int(file.read().strip())
    
    acolytes = 10
    available = 202400000
    
    heights = [1]
    width = 1
    currAmount = 1
    thickness = 1
    while currAmount < available:
        thickness = (thickness*nullpointers)%acolytes+acolytes
        width += 2
        heights.insert(0,0)
        heights.append(0)
        for i in range(len(heights)):
            heights[i] += thickness

        num_blocks = sum(heights)
        temp = nullpointers*width

        for i in range(1,len(heights)-1):
            removed_blocks = (temp*heights[i])%acolytes
            num_blocks -= removed_blocks
        currAmount = num_blocks

    return currAmount-available

def main():
    print("Hallo")
    print(dayEight(), "ist die Lösung von Teil 1")
    print(dayEight2(), "ist die Lösung von Teil 2")
    print(dayEight3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()