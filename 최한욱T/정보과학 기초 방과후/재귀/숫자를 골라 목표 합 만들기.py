import sys
sys.setrecursionlimit(10**5)

def answer(d, cs):
    if cs > S:
        return 0
    elif d == N:
        if cs == S:
            return 1
        else:
            return 0
    
    re = answer(d + 1, cs + Ns[d])
    re += answer(d + 1, cs)
    
    return re

N, S = map(int, input().split())
Ns = list(map(int, input().split()))

re = answer(0, 0)
if S == 0:
    re -= 1

print(re)