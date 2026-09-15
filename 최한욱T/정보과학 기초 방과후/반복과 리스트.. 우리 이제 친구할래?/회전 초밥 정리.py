N = int(input())
tmp = list(map(int, input().split()))

AN = tmp.copy() + tmp.copy()

last_piece = AN[0]
strick = 1
re = 0
for i in AN[1:]:
    if i == last_piece:
        strick += 1
    else:
        re = max(re, strick)

        last_piece = i
        strick = 1

re = max(re, strick)

print(min(N, re))