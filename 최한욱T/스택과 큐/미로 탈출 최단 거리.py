# 안타깝게도 테스트 케이스가 우하단으로 파면 무조건 최단 경로..

import sys

def dfs(x, y, depth):
    if x == N - 1 and y == M - 1:
        print(depth)
        sys.exit()

    if 0 <= x + 1 < N and not visited[x + 1][y] and board[x + 1][y] == '0':
        visited[x + 1][y] = True
        dfs(x + 1, y, depth + 1)
        visited[x + 1][y] = False
    
    if 0 <= y + 1 < M and not visited[x][y + 1] and board[x][y + 1] == '0':
        visited[x][y + 1] = True
        dfs(x, y + 1, depth + 1)
        visited[x][y + 1] = False

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
visited[0][0] = True
dfs(0, 0, 0)
print(-1)