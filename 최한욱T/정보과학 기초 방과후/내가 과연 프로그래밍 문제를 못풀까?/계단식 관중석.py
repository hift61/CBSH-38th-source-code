A, D, S = map(int, input().split())

total = 0
seat = A
n = 0
while total + seat <= S:
  total += seat
  n += 1
  seat += D

print(n)