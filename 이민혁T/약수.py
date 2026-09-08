N = int(input())

re = []
for i in range(1, N + 1):
    if N % i == 0:
        re.append(i)

print(*re, sep = ' ')
