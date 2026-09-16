import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
watched = [[False] * M for _ in range(N)]
def check(x, y):
    tg = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for tx, ty in tg:
        nx = x + tx
        ny = y + ty

        while 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1:
                break
            elif board[nx][ny] == 0:
                watched[nx][ny] = True

            nx += tx
            ny += ty

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            check(i, j)

re = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and not watched[i][j]:
            re += 1

print(re)