N = int(input())

tmp = [0]
while N % 2 == 0:
    N //= 2
    tmp[0] += 1

i = 3
while i * i <= N:
    cnt = 0
    while N % i == 0:
        N //= i
        cnt += 1

    if cnt >= 1:
        tmp.append(cnt)

    i += 1

if N > 1:
    tmp.append(1)

re = 1
for i in tmp:
    re *= (i + 1)

print(re)
