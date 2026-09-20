import sys
sys.setrecursionlimit(10**5)

def answer(d, cs):
    if d == N:
        if cs == K:
            return 1
        
        return 0
    
    re = answer(d + 1, cs + Ns[d])
    re += answer(d + 1, cs - Ns[d])

    return re

N, K = map(int, input().split())
Ns = list(map(int, input().split()))

print(answer(0, 0))