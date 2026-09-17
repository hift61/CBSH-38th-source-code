import sys
sys.setrecursionlimit(10**5)

def answer(ns, N):
    if ns == N:
        return 1
    elif ns > N:
        return 0
    
    re = 0
    for i in range(1, 3):
        re += answer(ns + i, N)
    
    return re

N = int(input())

print(answer(0, N))