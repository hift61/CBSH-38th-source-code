N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

re = 0
for i in range(0, N):
    for j in range(0, M):
        flag = True

        u_flag, d_flag, l_flag, r_flag = False, False, False, False

        # 오른쪽
        if 0 <= i < N - 1:
            r_flag = True

            if board[i + 1][j] >= board[i][j]:
                flag = False
        
        # 왼쪽
        if 0 < i <= N - 1:
            l_flag = True

            if board[i - 1][j] >= board[i][j]:
                flag = False
        
        # 위쪽
        if 0 < j <= M - 1:
            u_flag = True

            if board[i][j - 1] >= board[i][j]:
                flag = False
        
        # 아래쪽
        if 0 <= j < M - 1:
            d_flag = True

            if board[i][j + 1] >= board[i][j]:
                flag = False
        
        # l-u
        if l_flag and u_flag:
            if board[i - 1][j - 1] >= board[i][j]:
                flag = False
        
        # r-u
        if r_flag and u_flag:
            if board[i + 1][j - 1] >= board[i][j]:
                flag = False
        
        # l-d
        if l_flag and d_flag:
            if board[i - 1][j + 1] >= board[i][j]:
                flag = False
        
        # r-d
        if r_flag and d_flag:
            if board[i + 1][j + 1] >= board[i][j]:
                flag = False
        
        if flag:
            re += 1

print(re)
