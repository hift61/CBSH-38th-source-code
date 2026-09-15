N = int(input())
AN = list(map(int, input().split()))

last_num = AN[0]
strick = 1
re = -float('inf')
for i in AN[1:]:
    if i > last_num:
        last_num = i
        strick += 1
    else:
        re = max(re, strick)

        last_num = i
        strick = 1

re = max(re, strick)

print(re)