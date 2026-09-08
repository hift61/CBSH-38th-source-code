N = int(input())
ns = list(map(int, input().split()))

re = []
for i in range(N):
    for j in range(i + 1, N):
        re.append(ns[i] + ns[j])

print(len(set(re)))
