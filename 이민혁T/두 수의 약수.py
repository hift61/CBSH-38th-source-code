A, B = map(int, input().split())

re = []
for i in range(1, max(A, B) + 1):
    if A % i == 0 or B % i == 0:
        re.append(i)

print(*set(re), sep = ' ')
