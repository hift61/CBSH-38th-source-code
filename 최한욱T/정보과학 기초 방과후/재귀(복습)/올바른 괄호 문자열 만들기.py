import sys
sys.setrecursionlimit(10**5)

def answer(d, n):
    if n == 0:
        return 1

    if d == 0:
        return answer(1, n - 1)
    else:
        return answer(d + 1, n - 1) + answer(d - 1, n)

N = int(input())
print(answer(0, N))