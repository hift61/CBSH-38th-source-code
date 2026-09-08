import sys
input = sys.stdin.readline

N = int(input())

while N % 2 == 0:
    N //= 2

t = [1]
i = 3
while i * i <= N:
    cnt = 0
    while N % i == 0:
        N //= i
        cnt += 1

    if cnt > 0:
        t.append(cnt)

    i += 2

if N > 1:
    t.append(1)

re = 1
for i in t:
    re *= (i + 1)

print(re)
