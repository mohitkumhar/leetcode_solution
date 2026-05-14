from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    zeros = arr.count(0)
    ones = arr.count(1)
    twos = arr.count(2)

    idx = 0
    for _ in range(zeros):
        arr[idx] = 0
        idx += 1
    for _ in range(ones):
        arr[idx] = 1
        idx += 1
    for _ in range(twos):
        arr[idx] = 2
        idx += 1


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
