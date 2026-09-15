N = int(input())
AN = list(map(int, input().split()))

re = 0

situation = "up"
strick = 1
for i in range(1, N):
    if AN[i] > AN[i - 1]:
        if situation == "up":
            strick += 1
        else:
            situation = "up"
            strick = 2
    elif AN[i] < AN[i - 1]:
        if situation == "up":
            if strick >= 2:
                situation = "down"
                strick += 1
                re = max(re, strick)
            else:
                strick = 1
        else:
            strick += 1
            re = max(re, strick)
    else:
        situation = "up"
        strick = 1

print(re)