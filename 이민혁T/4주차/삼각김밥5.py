def sum(k):
  return k * (k + 1) // 2

N = int(input())
min = (N + 2) // 3
max = (N - 1) // 2

ans = 0
if min > max: print(ans)
else:
  tmp = (sum((N - min - 1) // 2) - sum(((N - max - 1) // 2 - 1))) * 2
  
  if (N - max - 1) % 2 == 1: tmp -= (N - max - 1) // 2
  if (N - min - 1) % 2 == 0: tmp -= (N - min - 1) // 2
  
  ans = sum(max) - sum(min - 1) - tmp
  print(ans)
