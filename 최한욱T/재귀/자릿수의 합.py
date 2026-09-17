import sys
sys.setrecursionlimit(10**5)

def answer(n):
    if n == 0:
        return 0
    
    return n % 10 + answer(n // 10)

N = int(input())

print(answer(N))