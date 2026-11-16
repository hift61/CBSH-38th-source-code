N, K = map(int, input().split())

l = [i for i in range(1, N + 1)]

while len(l) > 1:
    for _ in range(K - 1):
        l.append(l.pop(0))
    
    l.pop(0)

print(l[0])