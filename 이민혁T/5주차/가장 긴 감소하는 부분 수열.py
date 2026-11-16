N = int(input())
Ns = list(map(int, input().split()))

dp = [-1] * N
for i in range(N):
    dp[i] = 1
    for j in range(0, i):
        if Ns[j] > Ns[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))