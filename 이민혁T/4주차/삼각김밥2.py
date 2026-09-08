N = int(input())

re = 0
for i in range(1, N // 3 + 1):
  for j in range(i, N + 1):
    q = N - i - j
    
    if q > 0 and max([i, j, q]) == q and i + j > q:
      re += 1

print(re)