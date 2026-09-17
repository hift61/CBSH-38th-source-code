import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def answer(nx, ny):
    if nx == N - 1 and ny == M - 1:
        return 1
    
    re = 0

    tx, ty = (1, 0), (0, 1)
    for x, y in tx, ty:
        cx = nx + x
        cy = ny + y

        if 0 <= cx <= N - 1 and 0 <= cy <= M - 1:
            if not board[cx][cy]:
                re += answer(cx, cy)
    
    return re


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

print(answer(0, 0))