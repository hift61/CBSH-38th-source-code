A, B = map(int, input().split())

re = -float('inf')
for i in range(1, min(A, B) + 1):
    if A % i == B % i == 0:
        re = max(re, i)

print(re)
