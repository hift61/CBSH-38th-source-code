N = int(input())
Ns = list(map(int, input().split()))

re = []
for i in range(1, N - 1):
    if Ns[i - 1] < Ns[i] and Ns[i + 1] < Ns[i]:
        re.append(Ns[i])

if len(re) == 0:
    print(-1)
else:
    print(*re, sep = ' ')