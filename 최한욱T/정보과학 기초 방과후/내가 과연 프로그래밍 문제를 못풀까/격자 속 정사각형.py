N, M = map(int, input().split())

re = 0

for i in range(1, min(N, M) + 1):
    re += (N - i + 1) * (M - i + 1)

print(re)