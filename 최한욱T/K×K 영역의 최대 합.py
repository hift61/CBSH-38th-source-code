N, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

re = float('-inf')
for i in range(N - K + 1):
    for j in range(N - K + 1):
        tmp = 0
        
        for r in range(j, j + K):
            tmp += sum(board[r][i:i + K])

        re = max(re, tmp)

print(re)
