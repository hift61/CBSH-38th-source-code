N = int(input())
Ns = list(map(int, input().split()))

lis = [-1] * N
lds = [-1] * N

Ns_p = Ns[::-1]
for i in range(N):
    lis[i] = 1
    lds[i] = 1
    for j in range(i):
        if Ns[i] > Ns[j]:
            lis[i] = max(lis[i], lis[j] + 1)
        if Ns_p[i] > Ns_p[j]:
            lds[i] = max(lds[i], lds[j] + 1)

re = [0] * N
for i in range(N):
    re[i] = lis[i] + lds[N - i - 1] - 1

print(max(re))