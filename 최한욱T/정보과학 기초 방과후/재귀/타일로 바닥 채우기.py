import sys
sys.setrecursionlimit(10**5)

def answer(N):
    if N == 0:
        return 1
    if N < 0:
        return 0
    
    return answer(N - 1) + answer(N - 2)

N = int(input())

print(answer(N))