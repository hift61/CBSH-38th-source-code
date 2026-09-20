import sys
sys.setrecursionlimit(10**5)

def answer(cs, tmp):
    if cs == M:
        return 1
    elif cs > M:
        return 0
    
    re = 0
    for n in Ns:
        if len(tmp) == 0:
            re += answer(cs + n, tmp + [n])
        elif max(tmp) <= n:
            re += answer(cs + n, tmp + [n])
    
    return re

N, M = map(int, input().split())
Ns = list(map(int, input().split()))

print(answer(0, []))