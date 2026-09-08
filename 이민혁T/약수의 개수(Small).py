N = int(input())

re = 0
for i in range(1, N + 1):
    if N % i == 0:
        re += 1

print(re)
