import sys
sys.setrecursionlimit(10**5)

def answer(N):
    if N == 1:
        return 1
    elif N < 1:
        return 0
    
    re = 0
    if N % 2 == 0:
        re += answer(N // 2)
    if N % 3 == 0:
        re += answer(N // 3)
    
    return answer(N - 1) + re

N = int(input())

print(answer(N))