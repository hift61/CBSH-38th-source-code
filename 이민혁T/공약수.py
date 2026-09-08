A, B = map(int, input().split())

re = []
for i in range(1, min(A, B) + 1):
    if A % i == B % i == 0:
        re.append(i)

print(*re, sep = ' ')
