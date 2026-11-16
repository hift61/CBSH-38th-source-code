import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())

graph = {i: [] for i in range(1, N + 1)}
files = [0] * (N + 1)
re = [0] * (N + 1)

for i in range(1, N + 1):
    P, F = map(int, input().split())
    files[i] = F
    if P != 0:
        graph[P].append(i)

def answer(cp):
    tmp = files[cp]
    
    for np in graph[cp]:
        tmp += answer(np)
    
    re[cp] = tmp
    return tmp

answer(1)

for i in range(1, N + 1):
    print(re[i])