import sys
sys.setrecursionlimit(10**5)

def answer(n):
    if n < 1:
        return 0

    return n + answer(n - 1)

N = int(input())

print(answer(N))