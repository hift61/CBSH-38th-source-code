import sys
sys.setrecursionlimit(10**5)

def answer(ns, N):
    if ns == N:
        return 1
    elif ns > N:
        return 0
    
    return answer(ns + 1, N) + answer(ns * 2, N)

N = int(input())

print(answer(2, N))