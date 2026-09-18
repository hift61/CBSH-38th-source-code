N = int(input())

cnt = 0
for c in range(N // 3, (N - 1) // 2 + 1):
    min_a = max(1, N - 2 * c)
    max_a = (N - c) // 2

    if min_a <= max_a:
        cnt += max_a - min_a + 1

print(cnt)